class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {c: i for i, c in enumerate(order)}
        
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            flag = False
            for j in range(min(len(word1), len(word2))):
                if order_map[word1[j]] > order_map[word2[j]]:
                    return False
                elif order_map[word1[j]] < order_map[word2[j]]:
                    flag = True
                    break
            if not flag and len(word1) > len(word2):
                return False
        return True