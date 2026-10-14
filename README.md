# Huffman Zipper

A lightweight text compressor built with Python using Huffman coding.

This project demonstrates how to compress a file by counting character frequencies, building a Huffman tree, and storing the encoding table alongside the compressed bitstream. The companion decompressor reads that custom format and reconstructs the original text.

## ✨ What it does

- Counts repeated characters in a file
- Builds a Huffman tree from the frequency table
- Encodes the content using variable-length binary codes
- Saves a custom compressed binary format
- Decompresses the file back to readable text

## 🧩 Project structure

- [tree.py](tree.py) — Huffman tree logic, binary assignment, and tree display utilities
- [zip.py](zip.py) — compression script for creating `.zip`-style output files
- [unzip.py](unzip.py) — decompression script for reading the custom encoded format
- [LICENSE](LICENSE) — project license

## 🔧 How the compression works

1. Read the input file as text.
2. Count each character frequency.
3. Build a Huffman tree from the least frequent symbols upward.
4. Assign binary codes to each character.
5. Write a header containing the character-to-code mapping.
6. Store the compressed bit sequence after the header.

On decompression:

1. Read the header length from the first 4 bytes.
2. Parse the character/code dictionary.
3. Rebuild the original bitstream.
4. Decode the binary data back into readable text.

## 🚀 Usage

### Compress a file

```bash
python3 zip.py my_file.txt
```

This creates a new file named:

```bash
my_file.txt.zip
```

You can also pass multiple files at once:

```bash
python3 zip.py file1.txt file2.txt file3.txt
```

### Decompress a file

```bash
python3 unzip.py my_file.txt.zip
```

The script writes the extracted text to a file such as:

```bash
output0.unzip
```

## 📌 Important notes

- This is a custom Huffman encoder, not a full ZIP or gzip implementation.
- It is intended mainly as an educational project and a compact coding exercise.
- The implementation is designed for text-based data and may not be ideal for arbitrary binary files.

## 🧠 Example

If the source text is:

```text
hello world
```

The program counts the frequency of each character, generates Huffman codes, and writes a compressed binary stream containing both the code table and the encoded payload.

## ✅ Typical workflow

```bash
python3 zip.py sample.txt
python3 unzip.py sample.txt.zip
```

Then view the output file created by the decompressor.

---

This project is a simple and practical example of Huffman coding in Python, perfect for learning how lossless compression works under the hood.