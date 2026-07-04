class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str):
        current = self.root
        for c in word:
            current = current.children.setdefault(c, TrieNode())
        current.endOfWord = True
            
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words: return []
        result = []
        checked = set()
        row_count = len(board)
        col_count = len(board[0])

        def check(r, c, node, word):
            if r < 0 or r >= row_count or c < 0 or c >= col_count or (r,c) in checked or board[r][c] not in node.children: return
            current_char = board[r][c]
            current_word = word + current_char
            if node.children[current_char].endOfWord and current_word not in result:
                result.append(current_word)
            checked.add((r,c))
            check(r-1, c, node.children[current_char], current_word)
            check(r+1, c, node.children[current_char], current_word)
            check(r, c-1, node.children[current_char], current_word)
            check(r, c+1, node.children[current_char], current_word)
            checked.remove((r,c))
        
        for w in words: 
            self.addWord(w)
        
        for r in range(row_count):
            for c in range(col_count):
                check(r,c, self.root, "")
        
        return result
                