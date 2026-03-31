class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) 
        # key = charCount : value = list of anagrams

        for s in strs:
            count = [0] * 26 # a...z

            for c in s:
                count[ord(c) - ord("a")] += 1 # ord is ascii value so a - a = 0 and z - a = 25

            res[tuple(count)].append(s)

        return list(res.values())