class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        l = len(s)
        c = s.count(letter)
        return c*100//l