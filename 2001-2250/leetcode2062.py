class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a','e','i','o','u'}
        n = len(word)
        count = 0
        
        for i in range(n):
            vowel_set = set()
            for j in range(i, n):
                if word[j] in vowels:
                    vowel_set.add(word[j])
                    
                    if len(vowel_set) == 5:
                        count += 1
                else:
                    break
        
        return count