from PIL import (Image,
	ImageFont,
	ImageDraw)

from tree import (tree_height,
	tree_width,
	tree_height_px,
	tree_width_px)

from text import split_text_into_lines

RECTANGLE_WIDTH = 250
RECTANGLE_HEIGHT = 140
MARGIN_TOP = 25
MARGIN_LEFT = 35
PADDING = 30
OUTLINE_WIDTH = 5
COLOR_FILL = 1
COLOR_OUTLINE = 0
COLOR_LINE = 0
FONT_SIZE = 24
MAX_LINE_CHARACTERS = 14
LINE_WIDTH = 4
SUBTREE_MARGIN = 4 * MARGIN_LEFT

def subtree_image_size(root):
	depth = tree_width_px(root, RECTANGLE_WIDTH, MARGIN_LEFT) + 2 * PADDING
	height = tree_height_px(root, RECTANGLE_HEIGHT, MARGIN_TOP) + 2 * PADDING

	return (depth, height)

def create_function_hierarchy_diagram(root, font_filename):
	image_size_x = image_size_y = 0

	for child in root[1]:
		image_size_x += tree_width_px(child, RECTANGLE_WIDTH, MARGIN_LEFT) \
			+ SUBTREE_MARGIN
		image_size_y = max(image_size_y, tree_height_px(child, 
			RECTANGLE_HEIGHT, MARGIN_TOP))

	image_size_x = image_size_x - SUBTREE_MARGIN + 2 * PADDING
	image_size_y += 4 * MARGIN_TOP + 2 * PADDING + RECTANGLE_HEIGHT

	image = Image.new("1", (image_size_x, image_size_y), 1) # obiekt Image
	context = ImageDraw.Draw(image)
	font = ImageFont.truetype("font.ttf", FONT_SIZE)

	# prostokąt dla węzła głównego
	root_origin_x = (image_size_x - RECTANGLE_WIDTH) / 2
	root_origin_y = PADDING
	context.rectangle([root_origin_x, root_origin_y,
		root_origin_x + RECTANGLE_WIDTH, root_origin_y + RECTANGLE_HEIGHT],
		COLOR_FILL, COLOR_OUTLINE, OUTLINE_WIDTH)

	# tekst węzła głównego
	text = split_text_into_lines(root[0], MAX_LINE_CHARACTERS)
	context.multiline_text(
		(image_size_x / 2, PADDING + RECTANGLE_HEIGHT / 2), text, 0, font,
		"mm", align="center")

	# origin pierwszego poddrzewa
	subtree_origin_x = PADDING
	subtree_origin_y = PADDING + RECTANGLE_HEIGHT + 4 * MARGIN_TOP

	# współrzędne y linii pionowej od głównej linii poziomej do prostokąta
	# będącego korzeniem poddrzewa
	y0 = PADDING + RECTANGLE_HEIGHT + 2 * MARGIN_TOP
	y1 = y0 + 2 * MARGIN_TOP

	num_children = len(root[1])

	# rysowanie każdego poddrzewa
	for i, child in enumerate(root[1]):
		draw_subtree_node(context, (subtree_origin_x, subtree_origin_y),
			child, font)
		
		# współrzędne x linii pionowej od głównej linii poziomej do prostokąta
		# będącego korzeniem poddrzewa
		x0 = subtree_origin_x + RECTANGLE_WIDTH / 2
		x1 = x0
		context.line([x0, y0, x1, y1], COLOR_LINE, LINE_WIDTH)

		if i < num_children - 1:
			subtree_origin_x += tree_width_px(child, RECTANGLE_WIDTH,
				MARGIN_LEFT) + SUBTREE_MARGIN

	# główna linia pozioma
	x0 = PADDING + RECTANGLE_WIDTH / 2
	x1 = subtree_origin_x + RECTANGLE_WIDTH / 2
	y0 = y1 = PADDING + RECTANGLE_HEIGHT + 2 * MARGIN_TOP
	context.line([x0, y0, x1, y1], COLOR_LINE, LINE_WIDTH)

	# linia pionowa od głównego węzła do głównej linii poziomej
	x0 = x1 = image_size_x / 2
	y0 = root_origin_y + RECTANGLE_HEIGHT
	context.line([x0, y0, x1, y1], COLOR_LINE, LINE_WIDTH)

	image.show()
	return

def draw_subtree_node(draw_context, origin, node, font):
	x0 = origin[0]
	y0 = origin[1]
	x1 = x0 + RECTANGLE_WIDTH
	y1 = y0 + RECTANGLE_HEIGHT
	
	draw_context.rectangle([x0, y0, x1, y1], COLOR_FILL, COLOR_OUTLINE,
		OUTLINE_WIDTH)
	
	text = split_text_into_lines(node[0], MAX_LINE_CHARACTERS)

	draw_context.multiline_text(
		(x0 + RECTANGLE_WIDTH / 2, y0 + RECTANGLE_HEIGHT / 2), text, 0, font,
		"mm", align="center")

	x0 = x0 + 2 * MARGIN_LEFT
	y0 = y0 + RECTANGLE_HEIGHT + MARGIN_TOP

	num_children = len(node[1])

	if num_children == 0:
		return

	for i, child in enumerate(node[1]):
		draw_subtree_node(draw_context, (x0, y0), child, font)
		
		draw_context.line([x0, y0 + MARGIN_TOP, x0 - MARGIN_LEFT, 
			y0 + MARGIN_TOP], COLOR_LINE, LINE_WIDTH)
		
		if i < num_children - 1:
			y0 = y0 + tree_height_px(child, RECTANGLE_HEIGHT, MARGIN_TOP) \
				+ MARGIN_TOP

	x0 = x1 = origin[0] + MARGIN_LEFT
	y1 = y0 + MARGIN_TOP
	y0 = origin[1] + RECTANGLE_HEIGHT
	
	draw_context.line([x0, y0, x1, y1], COLOR_LINE, LINE_WIDTH)

	return