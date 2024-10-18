#Using Array
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        mWords = []
        count = 0

        for word in words:
            mCode = ''
            for w in word:
                mCode += morse[ord(w)-97]
            if mCode not in mWords:
                count += 1
                mWords.append(mCode)
        return count
    
#Using Dictionary and Set
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = {'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".", 'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---", 'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-", 'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.."}

        mWords = set()

        for word in words:
            mCode = ''
            for w in word:
                mCode += morse[w]
            
            mWords.add(mCode)
        return len(mWords)