class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        res = ''
        for i in range(len(word)):
            if word[i] == ch:
                res = word[:i+1][::-1]+word[i+1:]

                return res
        else:
            return word