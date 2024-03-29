def split_text_into_lines(text, line_max_length):
	text_length = len(text)
	result = ""
	i = line_max_length - 1
	j = 0

	while i < text_length:
		while i > j and text[i] != " ":
			i -= 1

		if i == j:
			raise Exception("There is word that is too long")

		if len(result) != 0:
			result += "\n"

		result += text[j:i]

		j = i + 1
		i = j + line_max_length - 1

	result += ("\n" if len(result) != 0 else "") + text[j:text_length]

	return result

def line_indent_level(line):
	i = 0
	
	while line[i] == "\t":
		i += 1

	return i
	