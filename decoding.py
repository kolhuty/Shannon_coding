class Node:
    def __init__(self, char=None):
        self.char = char
        self.left = None
        self.right = None

class Decode():
    def __init__(self, codes):
        self.root = Node()
        self.codes = codes

    def _build_tree(self):
        for char, code in self.codes.items():
            node = self.root
            for bit in code:
                if bit == '0':
                    if not node.left:
                        node.left = Node()
                    node = node.left
                else:
                    if not node.right:
                        node.right = Node()
                    node = node.right
            node.char = char

    def decoding(self, byte_text):
        """По построенному дереву кодов ищет наиболее "близкий" к коду из текста символ"""
        text = ''.join(f'{byte:08b}' for byte in byte_text)
        result = bytearray()
        self._build_tree()
        node = self.root
        for bit in text:
            node = node.left if bit == '0' else node.right
            if node.char is not None:
                result.append(node.char)
                node = self.root
        return bytes(result)