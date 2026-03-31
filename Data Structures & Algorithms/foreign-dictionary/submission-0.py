class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # create the adj list
        # for every word in our list of words
        # and for every char in each word
        # we want every char to be mapped to a set
        adj = { c:set() for w in words for c in w}

        # go thru every pair of words
        for i in range(len(words) - 1):
            # get two words
            w1, w2 = words[i], words[i + 1]

            # get min length b/w the words
            minLen = min(len(w1), len(w2))

            # check edge case: prefix of words is the same
            # but the first word is longer than second
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            # go thru every char b/w these words
            for j in range(minLen):
                # goal: find first differing char
                if w1[j] != w2[j]:
                    # add this instance to our adj list
                    adj[w1[j]].add(w2[j])

                    # we are breaking because we only want
                    # the first one, no more than that
                    break

        # start doing DFS
        # keep track of visited nodes
        visit = {} # False=Visited, True=visited & in curr path
        res = []


        def dfs(c):
            # if we already did this char
            if c in visit:
                return visit[c]
                # this can return False or True based on conditions above
                # if it return True that means we have seen this char 
                # twice in current path and we detected a loop/cycle

            # mark char as being in current path
            visit[c] = True

            # go thru every char that is a nei of c
            for nei in adj[c]:
                # run DFS on that neighbor
                if dfs(nei):
                    # there was a loop so return True
                    return True

            visit[c] = False


            res.append(c)

        # for some reason we build result in reverse order
        
        for c in adj:
            if dfs(c):
                # detected a cycle/loop
                return ""

        # result is list and reversed so we gotta fix that
        res.reverse()
        return "".join(res)

        