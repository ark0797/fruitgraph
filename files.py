import sys
param = sys.argv
if len(param) > 1:
	param[:] = param[1:]
	for name in param:
		files = open(name,"r")
		txt = files.readlines()
		for x in txt:
			print(x)
		files.close()
else:
	print("Too small numbers")
