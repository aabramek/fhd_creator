#!python3

import sys

def line_indent_level(line):
	i = 0
	
	while line[i] == "\t":
		i += 1

	return i


def load_tree_from_file(filename, rootname):
	lines = []
	try:
		file = open(filename)
		lines = file.readlines()
		file.close()
	except OSError:
		print("Failed to open file")

	recent_indent_level = 0
	recent_node_at_indent = [(rootname, [])]
	
	for line_number, line in enumerate(lines):
		indent_level = line_indent_level(line) + 1
		
		if indent_level > recent_indent_level + 1:
			print("Line #{} has inappropriate indent level ({}), ignoring".format(line_number, indent_level), file = sys.stderr)
			continue

		line = line.strip()
		new_node = (line, [])
		
		recent_node_at_indent[indent_level - 1][1].append(new_node)
	
		if indent_level > len(recent_node_at_indent) - 1:
			recent_node_at_indent.append(new_node)
		else:
			recent_node_at_indent[indent_level] = new_node

		recent_indent_level = indent_level

	return recent_node_at_indent[0]

def print_tree(root, depth = 0):
	print(" " * depth + root[0])
	for child in root[1]:
		print_tree(child, depth + 1)
	return

def tree_depth(root):
	if len(root[1]) == 0:
		return 0

	children_depths = []
	
	for child in root[1]:
		children_depths.append(tree_depth(child) + 1)

	return max(children_depths)

if len(sys.argv) < 4:
	print("Usage: fhd.py <system name> <data file name> <output image name>")
	exit(1)

root = load_tree_from_file(sys.argv[2], sys.argv[1])
print(tree_depth(root))

