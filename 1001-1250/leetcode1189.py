class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        charatext = Counter(text)
        balloon = Counter("balloon")
        result = len(text)
        for i in balloon :
            result = min(result,charatext[i] // balloon[i])
        return result