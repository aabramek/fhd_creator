from PIL import Image, ImageFont, ImageDraw

from tree import tree_height, tree_depth

from text_tools import split_text_into_lines

RECTANGLE_WIDTH = 250
RECTANGLE_HEIGHT = 140
MARGIN_TOP = 25
MARGIN_LEFT = 35
PADDING = 30
OUTLINE_WIDTH = 5
COLOR_FILL = 1
COLOR_OUTLINE = 0 
FONT_SIZE = 24
MAX_LINE_CHARACTERS = 14
LINE_WIDTH = 4

def subtree_image_size(root):
	depth = tree_depth(root)
	height = tree_height(root)

	return (((depth - 1) * MARGIN_LEFT * 2 + RECTANGLE_WIDTH) + 2 * PADDING,
		height * (RECTANGLE_HEIGHT + MARGIN_TOP) + 2 * PADDING)

def create_tree_image(root, font_filename):
	image = Image.new("1", subtree_image_size(root), 1) # obiekt Image
	context = ImageDraw.Draw(image)
	font = ImageFont.truetype("font.ttf", FONT_SIZE)
	draw_subtree_node(context, (PADDING, PADDING), root, font)
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
			y0 + MARGIN_TOP], 0, LINE_WIDTH)
		
		if i < num_children - 1:
			y0 = y0 + tree_height(child) * (RECTANGLE_HEIGHT + MARGIN_TOP)

	x0 = x1 = origin[0] + MARGIN_LEFT
	y1 = y0 + MARGIN_TOP
	y0 = origin[1] + RECTANGLE_HEIGHT
	
	draw_context.line([x0, y0, x1, y1], 0, LINE_WIDTH)

	return