
class Tree_Node:
    def __init__(self, chars=None, freq=0, left=None, right=None):
        self.chars = chars
        self.freq = freq
        self.left = left
        self.right = right

def optimal_separation(freq: dict) -> int:
    """Find the most optimal index for separation"""
    total = sum(freq for _, freq in freq)
    half = total / 2
    count_freq = 0
    min_diff = float('inf')
    index = 0

    for i, (_, freq) in enumerate(freq):
        count_freq += freq
        current_diff = abs(count_freq - half)
        if current_diff < min_diff:
            min_diff = current_diff
            index = i
        else:
            break

    return index

def build_shanon_tree(freq: dict) -> Tree_Node:
    """Build Shanon Tree"""
    if len(freq) == 1:
        char, freq = freq[0]
        return Tree_Node(chars=[char], freq=freq)

    sep_index = optimal_separation(freq)
    left_node = build_shanon_tree(freq[:sep_index+1])
    right_node = build_shanon_tree(freq[sep_index+1:])

    return Tree_Node(chars=left_node.chars + right_node.chars, freq=left_node.freq + right_node.freq, left=left_node, right=right_node)

def coding(node: Tree_Node, prefix="", codes={}) -> dict:
    """Encoding Shanon Tree"""
    if node.left is None and node.right is None:
        for char in node.chars:
            codes[char] = prefix
        return codes

    if node.left:
        coding(node.left, prefix + "0", codes)
    if node.right:
        coding(node.right, prefix +"1", codes)

    return codes