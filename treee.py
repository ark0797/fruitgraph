import sys
import os
path = str(sys.argv[0])
if os.path.exists(path):	
	tree = os.listdir(path)
	print(tree)
else:
	print("This path is not real! Try another path!")
