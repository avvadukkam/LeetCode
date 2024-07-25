# BruteForce
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStr = []
        res = []
        for i in strs:
            a = sorted(i)
            if a not in sortedStr:
                sortedStr.append(a)
                res.append([i])
            else:
                res[sortedStr.index(a)].append(i)
        return res
    

# Proper
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0]*26

            for c in s:
                count[ord(c)-ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()
    
# OR
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res  = defaultdict(list)
        for word in strs:
            sorted_word = tuple(sorted(word))
            res[sorted_word].append(word)
        return list(res.values())