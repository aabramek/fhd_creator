from text import line_indent_level

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

def tree_width(root):
	depth = 0
	
	for child in root[1]:
		depth = max(depth, tree_width(child))

	return depth + 1

def tree_height(root):
	height = 0

	for child in root[1]:
		height += tree_height(child)

	return height + 1

def tree_width_px(root, width, margin):
	w = tree_width(root)
	return width + (w - 1) * 2 * margin

def tree_height_px(root, height, margin):
	h = tree_height(root)
	return h * (height + margin) - margin
