# define a Trie node class
class TrieNode:
	def __init__(self):
		# for each char, it is going to be char : TrieNode
		self.children = {}

		# need to designate if it is the end of a word
		self.word = False

class WordDictionary:

    def __init__(self):
        # define root as a TrieNode
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        # set current = root because that is where we are going to start
        cur = self.root
        
        # this is inserting every char from this word into our trie
        for c in word:
            # check if char is not already inserted
            if c not in cur.children:
                # then we insert it
                cur.children[c] = TrieNode() # makes char : TrieNode

                # update current pointer to this new Trie node
            cur = cur.children[c]
            
        # designating the last char as end of word
        cur.word = True

    def search(self, word: str) -> bool:
	
        def dfs(j, root):
            cur = root
        
            # go thru every single char in word
            for i in range(j, len(word)):
                c = word[i]
            
                # if this char is a .
                if c == ".":
                    # we are going to use backtracking / recursion to help us explore 26 paths
                    # we want only the values because those are going to be the actual children
                    for child in cur.children.values():
                        # for each child, we want to do the recursion on it AKA DFS
                        # want to know the remaining portion of the word we are trying to match
                        # so we are going to pass in the starting index of that portion, i + 1
                        # and the current node we are at, which is the current child
                        # if this function ends up returning True, that means we found one valid path
                        if dfs(i + 1, child):
                            # so we can return True and exit
                            return True

                    # if we never find a match then we are going to return False
                    return False
                    

                else:
                    # c is a regular char
                    # check that c is not in cur.children because that means this character does not exist
                    if c not in cur.children:
                        # we needed it to exist, it doesn't so return False
                        return False

                    # if the char does exist then we shift the current pointer to that node
                    cur = cur.children[c]
                
            # if cur.word is True, then we return True because we reached and have found a valid word
            return cur.word

        # call DFS function
        # pass in 0 because we are always going to start at the beginning of a word
        # pass in self.root because we are always going to start at the root node of our trie
        return dfs(0, self.root)
            
