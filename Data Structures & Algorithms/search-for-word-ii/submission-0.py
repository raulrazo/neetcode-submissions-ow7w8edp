# implement a Trie Node class
class TrieNode:
    def __init__(self):
        # key is going to be the character and value is going to be the trie node
        self.children = {}

        # to mark if it is the end of a word
        self.isWord = False

    def addWord(self, word):
        # current ptr is set to root node
        cur = self

        # go char by char in this word and start adding to Trie
        for c in word:
            # if the char does not exist in our Trie
            if c not in cur.children:
                # we insert it
                cur.children[c] = TrieNode()

            # if the char already exist then we move that cur ptr to that position
            cur = cur.children[c]

        # we are at the last char so we mark that this is going to be the end of the word
        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # create a root trie node
        root = TrieNode()

        # take each word and add it to our Trie
        for w in words:
            root.addWord(w)

        # start doing DFS
        # get dimensions of the board
        ROWS, COLS = len(board), len(board[0])
        
        # result set is going to be set of words
        # visit set is for not getting stuck in an infinite loop during dfs
        # so we don't repeat the same character twice

        res, visit = set(), set()
        

        def dfs(r, c, node, word):
            # define base cases

            # if we go out of bounds or position has already been visited or the char is not in our Trie 
            # (meaning it is not one of the word we were given in our input list of words)
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or 
                (r, c) in visit or board[r][c] not in node.children):
                return

            # mark position as visited
            visit.add((r,c))

            # node is set to node.children of the cur char we just visited
            node = node.children[board[r][c]]

            # add new char we just reached to the word
            word += board[r][c]

            # check if this is the end of a word
            if node.isWord:
                # if it is then we update our result
                res.add(word)

            # call our recursive shit in all directions
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            # mark this an unvisited because this is backtracking
            # and we can visit the same one twice
            visit.remove((r,c))

        # go thru every position in the grid and do that dfs
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        # since our result is a set to eliminate duplicates, we turn it into a set
        return list(res)
