class Solution:
    def countValidWords(self, sentence: str) -> int:
        def is_valid_word(word):
            if any(char.isdigit() for char in word):
                return False
            
            hyphen_count = word.count('-') 
            if hyphen_count > 1:
                return False
            if hyphen_count == 1:
                hyphen_index = word.index('-')
                if hyphen_index == 0 or hyphen_index == len(word) - 1:
                    return False
                if not (word[hyphen_index - 1].isalpha() and word[hyphen_index + 1].isalpha()):
                    return False   

            punctuations = set("!.,")
            punctuation_count = sum(1 for char in word if char in punctuations)
            if punctuation_count > 1:
                return False
            if punctuation_count == 1 and word[-1] not in punctuations:
                return False
            
            return True

        words = sentence.split()

        return sum(1 for word in words if is_valid_word(word))
