from tree import *
import sys

def read_header(text):
	header_size = int.from_bytes(text[:4], "big")
	keys = {}
	raw_header = text[4:header_size+4].decode("utf-8")
	i = 0
	active_char = ""
	active_bin = ""
	while i < len(raw_header):
		if raw_header[i] == ' ' and not (i > 0 and raw_header[i-1] == ' '):
			keys[active_bin] = active_char
			active_char = ""
			active_bin = ""
			i+=1
			continue
		if active_char == "":
			active_char = raw_header[i]
			i+=1
			continue
		active_bin += raw_header[i]
		i+=1
	return keys, "".join(format(byte, "08b") for byte in text[header_size+4:])


def unzip_file(text: str):
	# print(text)

	decode_keys, text_binary = read_header(text)
	final_text = ""
	bin = ""
	for b in text_binary:
		bin += b
		c = decode_keys.get(bin, None)
		if len(bin) > 20:
			break
		if c:
			final_text += c
			bin = ""
	return final_text

if __name__ == "__main__":
	if len(sys.argv) == 1:
		print("Error: No file turned in", file=sys.stderr)
		print("Command use: python3 unzip.py file1 file2 ...", file=sys.stderr)
		exit()

	for i in range(1, len(sys.argv)):
		with open(sys.argv[i], 'rb') as file:
			content = file.read()
			new_content = unzip_file(content)
			if not new_content:
				print("Error while zipping the file")
				continue
			new_file = open(f"output{i-1}.unzip", "w")
			new_file.write(new_content)
