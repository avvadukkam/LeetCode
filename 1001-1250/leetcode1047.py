class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = ['']
        for l in s:
            if res[-1]!=l:
                res.append(l)
            else:
                res.pop()
        return ''.join(res)