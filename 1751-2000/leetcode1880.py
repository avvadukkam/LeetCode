class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def wordToNum(word):
            return int(''.join(str(dic[ch]) for ch in word))
        
        dic = {'a':'0','b':'1','c':'2','d':'3','e':'4',
                'f':'5','g':'6','h':'7','i':'8','j':'9'}
        num1 = wordToNum(firstWord)
        num2 = wordToNum(secondWord)
        targetNum = wordToNum(targetWord)
        
        return num1 + num2 == targetNum