#!python3

from PIL import Image, ImageFont, ImageDraw

import sys
import tree

def create_node_box(node):

	return

if len(sys.argv) < 5:
	print("Usage: fhd.py <system name> <font file name> <data file name> <output image name>")
	exit(1)

root = tree.load_tree_from_file(sys.argv[3], sys.argv[1])

