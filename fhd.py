#!python3

import os
import sys
import tree
import image

if len(sys.argv) < 3:
	print("Usage: fhd.py <data file name> <output image name>")
	exit(1)

data_file_name = sys.argv[1]
output_file_name = sys.argv[2]
root_name = os.path.basename(data_file_name[:data_file_name.index(".")])
root = tree.load_tree_from_file(data_file_name, root_name)
diagram = image.create_function_hierarchy_diagram(root)
diagram.save(output_file_name)
