class TrieNode:
    def __init__(self):
        self.isWord = False
        # 字符串仅由小写英文字符组成，若没有这个限制，就不能用数组来存储字符，而使用哈希表
        self.children = [None] * 26


# 字典树 用于处理字符串集合，例如用于高效地存储和检索字符串数据集中的键
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if cur.children[idx] is None:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if cur.children[idx] is None:
                return False
            cur = cur.children[idx]
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            idx = ord(char) - ord('a')
            if cur.children[idx] is None:
                return False
            cur = cur.children[idx]
        return True
