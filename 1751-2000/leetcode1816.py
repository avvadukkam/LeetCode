class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        temp = s.split()
        return ' '.join(temp[:k])
         

# OR

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split()[:k])
         