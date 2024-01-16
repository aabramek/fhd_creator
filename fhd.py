#!python3

import sys
import tree
import image

if len(sys.argv) < 4:
	print("Usage: fhd.py <system name> <data file name> <output image name>")
	exit(1)

root = tree.load_tree_from_file(sys.argv[2], sys.argv[1])

image.create_tree_image(root, sys.argv[1])

