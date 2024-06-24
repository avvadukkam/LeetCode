class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        d = {chr(i+96):0 for i in range(1,27)}
        for i in chars:
            d[i]+=1
        for i in words:
            for j in i:
                if d[j] < i.count(j):
                    break
            else:
                result += len(i)
        return result