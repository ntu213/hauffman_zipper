
class Node:

	def __init__(self, char, bin, weight, left=None, right=None):
		self.char = char
		self.bin = bin
		self.weight = weight
		self.left = left
		self.right = right

	def normalized_char(self):
		cases = {
			"\0": "EOF",
			" ": "SPACE",
			None: "┐"
		}
		return cases.get(self.char, repr(self.char)[1:-1])
	
	def normalized_bin(self):
		cases = {
			None: "┐"
		}
		return cases.get(self.bin, self.bin)

	def show_self(self):
		print(f"Char: {self.normalized_char()}, Binary: {self.bin}, Weight: {self.weight}")

	def tree(self):
		return ({
			"char": self.char,
			"bin": self.bin,
			"weight": self.weight,
			"left": self.left.tree() if self.left else None,
			"right": self.right.tree() if self.right else None
		})

	def show_tree(self, data: str = "char", show_weights: bool = False):

		if data not in ["char", "bin", "all"]:
			print("Error: Wrong Data Type")
			return

		def recursive_tree_print(node: Node, depth = 0, prefix = ""):
			if not node:
				return None

			if depth < 1:
				prefix = ""

			line2 = recursive_tree_print(node.right, depth=depth+1, prefix = prefix + "   ")
			line1 = ""
			if line2:
				line1 = recursive_tree_print(node.left, depth=depth+1, prefix = prefix + "│  ")
			else:
				line1 = recursive_tree_print(node.left, depth=depth+1, prefix = prefix + "   ")

			char = node.normalized_char()
			if data == "bin":
				char = node.normalized_bin()
			elif data == "all" and node.bin:
				char += "-" + node.normalized_bin()

			res = char + (f"-{node.weight}" * show_weights * bool(node.char)) + "\n"
			if line1:
				s = ""
				if not line2:
					s = "└──"
				else:
					s = "├──"
				s += line1
				res += prefix + s
			if line2:
				res += prefix + "└──" + line2

			return res

		print(recursive_tree_print(self))

	def reduce(self):
		data = {self.char:self.bin}
		if self.left:
			data.update(self.left.reduce())
		if self.right:
			data.update(self.right.reduce())
		return data


def build_tree_write(data: dict) -> Node:
	nodes = [Node(key, "", value) for key, value in data.items()]

	if len(nodes) < 2:
		if not len(nodes):
			return None
		nodes[0].bin = "0"
		return nodes[0]

	def assign_binary(node: Node, id: str = "", in_loop = False):
		if not node:
			return
		if node.char:
			node.bin = id
		assign_binary(node.left, id+"0", in_loop=True)
		assign_binary(node.right, id+"1", in_loop=True)

	# nodes = sorted(nodes, key=lambda x: x.weight)
	# [node.show_self() for node in nodes]
	while len(nodes) > 1:
		nodes = sorted(nodes, key=lambda x: x.weight, reverse=True)
		pop = nodes[-2:]
		total_weight = sum([e.weight for e in pop])
		new = Node(None, None, total_weight, left=pop[0], right=pop[1])
		nodes = nodes[:-2] + [new]

	assign_binary(nodes[0])

	# print(json.dumps(nodes[0].tree(), indent=2))
	nodes[0].show_tree(show_weights=True, data="all")

	return (nodes[0])

# build_tree_write({'a': 5, 'b': 1, 'd': 3, 'c': 6})

