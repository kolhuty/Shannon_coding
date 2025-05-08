class TreeNode:
    def __init__(self, chars: list[str] = None, freq: int = 0, left=None, right=None):
        self.chars = chars or []
        self.freq = freq
        self.left = left
        self.right = right


class Encode:
    def __init__(self, frequency_dict: dict[str, int]):
        self.sorted_freq = sorted(
            frequency_dict.items(),
            key=lambda x: (-x[1], x[0])
        )
        self.tree = self._build_tree(self.sorted_freq)
        self.codes = self._generate_codes()

    @staticmethod
    def _optimal_split(sorted_freq: list[tuple[str, int]]) -> int:
        """
        Ищет такой индекс, при котором символы полученного алфавита делят на две части,
        суммарные вероятности символов которых максимально близки друг другу.
        """
        total = sum(freq for _, freq in sorted_freq)
        half = total / 2
        current_sum = 0
        best_index = 0
        min_diff = float('inf')

        for i, (char, freq) in enumerate(sorted_freq):
            current_sum += freq
            current_diff = abs(current_sum - half)
            if current_diff < min_diff:
                min_diff = current_diff
                best_index = i
            else:
                break
        return best_index

    def _build_tree(self, freq_data: list[tuple[str, int]]) -> TreeNode:
        if len(freq_data) == 1:
            char, freq = freq_data[0]
            return TreeNode(chars=[char], freq=freq)

        split_idx = self._optimal_split(freq_data)
        left = self._build_tree(freq_data[:split_idx + 1])
        right = self._build_tree(freq_data[split_idx + 1:])

        return TreeNode(
            chars=left.chars + right.chars,
            freq=left.freq + right.freq,
            left=left,
            right=right
        )

    def _generate_codes(self) -> dict[str, str]:
        codes = {}

        def traverse(node: TreeNode, code: str = ""):
            """Рекурсивная функция, которая по дереву строит оптиммальные коды"""
            if not node.left and not node.right:
                for char in node.chars:
                    codes[char] = code
                return
            if node.left:
                traverse(node.left, code + "0")
            if node.right:
                traverse(node.right, code + "1")

        traverse(self.tree)
        return codes

    def get_codes(self) -> dict[str, str]:
        return self.codes.copy()