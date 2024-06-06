class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [set("qwertyuiop"),set("asdfghjkl"),set("zxcvbnm")]
        def can_be_typed(word):
            word_set = set(word.lower())
            for row in rows:
                if word_set.issubset(row):
                    return True
            return False
        
        return [word for word in words if can_be_typed(word)]