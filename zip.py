from tree import *
import sys, collections

def create_header(data: dict):
	header = ""
	for key, value in data.items():
		header += f"{key}{value} "
	return header

def zip_file(text: str):

	data = build_tree_write(dict(collections.Counter(text)))
	reduced_data = data.reduce()
	reduced_data.pop(None)
	print(reduced_data)

	# header = json.dumps(reduced_data).encode("utf-8")
	header = create_header(reduced_data).encode("utf-8")
	binary_data = len(header).to_bytes(4, "big")
	binary_data += header

	bits = ""
	for c in text:
		bits += reduced_data[c]

	binary_data += bytes(
		int(bits[i:i + 8], 2)
		for i in range(0, len(bits), 8)
	)
	return binary_data

if __name__ == "__main__":
	if len(sys.argv) == 1:
		print("Error: No file turned in", file=sys.stderr)
		print("Command use: python3 zip.py file1 file2 ...", file=sys.stderr)
		exit()

	for i in range(1, len(sys.argv)):
		with open(sys.argv[i], 'r') as file:
			content = file.read()
			new_content = zip_file(content)
			if not new_content:
				print("Error while zipping the file")
				continue
			new_file = open(sys.argv[i]+".zip", "wb")
			new_file.write(new_content)




# with open("compressed.bin", "wb") as f:
#     header = json.dumps(codes).encode("utf-8")
#     f.write(len(header).to_bytes(4, "big"))
#     f.write(header)

# Your file now contains:

# +-----------------------+
# | Header length (4 B)   |
# +-----------------------+
# | Huffman dictionary    |
# +-----------------------+
# | Compressed bits       |
# +-----------------------+

# To read the dictionary:

# with open("compressed.bin", "rb") as f:
#     header_size = int.from_bytes(f.read(4), "big")
#     header = f.read(header_size)
#     codes = json.loads(header.decode("utf-8"))
