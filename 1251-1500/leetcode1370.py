class Solution:
    def sortString(self, s: str) -> str:
        letterSet = set(s)
        freq = {}
        res = ""
        ref = sorted(set(s))
        for i in letterSet:
            freq[i] = s.count(i)
        while len(res) != len(s):
            for i in ref:
                if i in freq and freq[i] > 0:
                    res += i
                    freq[i] -= 1
            for i in ref[::-1]:
                if i in freq and freq[i] > 0:
                    res += i
                    freq[i] -= 1
        return res