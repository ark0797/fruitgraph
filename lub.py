import networkx as nx
import matplotlib.pyplot as plt

class graf_analiz():
    def grafs(self):
        N = int(input("Введите количество вершин: "))
        M = int(input("Введите количество рёбер: "))
        g = {}
        for i in range(N):
            g[str(i)] = {}
        for i in range(M):
            a,b,weight = input("Введите ребро через вершины с весом: ").split()
            g[a][b] = weight
        return(g)

    def graf(self):
        mat = open("./mat.txt","r")
        matt = mat.readlines()
        g = {}
        j = 0
        sp = str(matt[j]).replace("\n","").split()
        while len(sp) == 1:
            g[str(matt[j]).replace("\n","")] = {}
            j += 1
            sp = str(matt[j]).replace("\n","").split()
        for i in range(j,len(matt)):
            a,b,weight = str(matt[i]).replace("\n","").split()
            g[a][b] = float(weight)
            g[b][a] = float(weight)
        return(g)

    def __init__(self):
        a = None
        b = None
        func = None
        #func = input("Введите функцию: ")
        a,b = self.DFS("1")
        self.draws(a,b,"DFS")
        a,b,c,l = self.BFS("1",self.graf())
        self.draws(a,b,"BFS")
        self.komp_sviaz("1",self.graf())
        self.shortest_length("1",self.graf())
        a,b = self.shortest_path("1",self.graf(),"5")
        self.draws(a,b,"SP")
        if func == "DFS":
            a,b = self.DFS("1")
        elif func == "BFS":
            a,b,c,l = self.BFS("1",self.graf())
        elif func == "KS":
            self.komp_sviaz("1",self.graf())
        elif func == "SL":
            self.shortest_length("1",self.graf())
        elif func == "SP":
            a,b = self.shortest_path("1",self.graf(),"5")
        #if a:
        #   self.draws(a,b)

    def DFS(self,start):
        mat = self.graf()
        fired = []
        list = []
        g = nx.Graph()
        G,ls = self.recur(mat,start,fired,list,g)
        return g,ls

    def BFS(self,start,mat):
        queue = [start]
        fired = [start]
        list = []
        g = nx.Graph()
        g.add_node(start)
        shortest_path_length = {versh:float("+inf") for versh in mat}
        shortest_path_length[start] = 0
        while queue:
            star = queue.pop(0)
            for neibours in mat[star]:
                new_shortest_path_length = shortest_path_length[star] + mat[star][neibours]
                if new_shortest_path_length < shortest_path_length[neibours]:

                    shortest_path_length[neibours] = new_shortest_path_length
                if neibours not in fired:
                    queue.append(neibours)
                    fired.append(neibours)
                    g.add_edge(star,neibours)
                    list.append((star,neibours))

        return g,list,mat,shortest_path_length

    def shortest_path(self,start,mat,end):
        shortest_leng = {vert:float("+inf") for vert in mat}
        shortest_path = {vert:[] for vert in mat}
        queue = [start]
        fired = [start]
        shortest_leng[start] = 0
        while queue:
            star = queue.pop(0)
            for neibours in mat[star]:
                new_shortest_path_length = shortest_leng[star] + mat[star][neibours]
                if neibours not in fired:
                    queue.append(neibours)
                    fired.append(neibours)
                if new_shortest_path_length < shortest_leng[neibours]:
                    shortest_leng[neibours] = new_shortest_path_length
                    shortest_path[neibours] = (star,neibours)
        x = shortest_path[end]
        path = []
        path.insert(0,x)
        g = nx.Graph()
        g.add_edge(x[0],x[1])
        while x[0] != start:
            path.insert(0,shortest_path[x[0]])
            x = shortest_path[x[0]]
            g.add_edge(x[0],x[1])
        return g,path


    def komp_sviaz(self,start,mat):
        g,ls,G,l = self.BFS(start,mat)
        lsG = [(g,ls)]
        if len(g) < len(G):
            for x in G:
                for y in range(len(lsG)):
                    if x in lsG[y][0]:
                        break
                else:
                    a,b,c,l = self.BFS(x,mat)
                    lsG.append((a,b))
        self.drawss(lsG)

    def shortest_length(self,start,mat):
        a,b,c,length = self.BFS(start,mat)
        sl = open("SL.txt","w")
        for i in length:
            if length[i] != float("+inf"):
                #print("Расстояние из", start,"в",i,"равно",length[i])
                sl.write(str(i)+":"+str(length[i])+"\n")
            else:
                #print("Из",start,"в",i,"нет пути.")
                pass

    def draws(self,G,listed,func):
        listn = []
        pos = nx.spring_layout(G)
        for i in G:
            listn.append(i)
        nx.draw_networkx_nodes(G,pos,nodelist=listn,node_color='b',node_size=200,alpha=0.8)
        nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)
        nx.draw_networkx_edges(G,pos,edgelist=listed,width=2,alpha=0.5,edge_color='r')
        nx.draw_networkx_labels(G,pos,font_size=16)
        plt.axis('off')
        name = str(func) + ".png"
        plt.savefig(name)
        plt.show()
    def drawss(self,lsG):
        edgec = ['r','b','g','y','w']
        for x in range(len(lsG)):
            listn = []
            pos = nx.spring_layout(lsG[x][0])
            for i in lsG[x][0]:
                listn.append(i)
            nx.draw_networkx_nodes(lsG[x][0],pos,nodelist=listn,node_color=edgec[x],node_size=200,alpha=0.8)
            nx.draw_networkx_edges(lsG[x][0],pos,width=1.0,alpha=0.5)
            nx.draw_networkx_edges(lsG[x][0],pos,edgelist=lsG[x][1],width=2,alpha=0.5,edge_color=edgec[x])
            nx.draw_networkx_labels(lsG[x][0],pos,font_size=16)
        plt.axis('off')
        plt.savefig("KS.png")
        plt.show()

    def recur(self,G,start,f,list,g):
        f.append(start)
        for neibours in G[start]:
            if neibours not in f:
                list.append((start,neibours))
                g.add_edge(start,neibours)
                self.recur(G,neibours,f,list,g)
        return g,list
analitic = graf_analiz()
