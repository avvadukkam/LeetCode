class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ['a','e','i','o','u']
        sentence = sentence.split()
        for i in range(len(sentence)):
            if sentence[i][0].lower() in vowels:
                sentence[i] = sentence[i] + 'ma'
            else:
                sentence[i] = sentence[i][1:] + sentence[i][0] + 'ma'
            sentence[i] = sentence[i] + 'a'* (i+1)
        return ' '.join(sentence)