
class Node:
    def __init__(self, char=None):
        self.char = char
        self.left = None
        self.right = None

def build_tree(codes: dict):
    root = Node()
    for char, code in codes.items():
        node = root
        for bit in code:
            if bit == '0':
                node.left = Node()
                node = node.left
            else:
                node.right = Node()
                node = node.right
        node.char = char
    return root

def decoding(byte_text, root):
    text = ''.join(f'{byte:08b}' for byte in byte_text)

    result = bytearray()
    node = root
    for bit in text:
        node = node.left if bit == '0' else node.right
        if node.char:
            result.append(node.char)
            node = root
    return bytes(result)