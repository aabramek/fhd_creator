# FHD Creator

Simple script for creating function hierachy diagrams

## How to use it 

python fdh\.py **\<data file name\>** **\<output file name\>**

**data file name** - name of file that consists text in following scheme:

- function_1
	- function_1_1
	- function_1_2
		- function_1_2_1
		- function_1_2_2
	- function_1_3
	- function_2
- function_2

Indentations in file must be done with tab character (0x09), not with spaces (0x20).
Lines with improper identation level are ignored.

Name of the root node in the diagram is base name (path ommited)
of this file without an extension eg:
- "file.txt" gives name "file"
- "C:\\users\\user\\file.txt" also give name "file"

**output file name** - name of file to be created. Image representing created diagram.
