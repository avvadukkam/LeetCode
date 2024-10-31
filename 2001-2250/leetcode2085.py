class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count = 0
        for word in words1:
            if word in words2 and words1.count(word) == 1 and words2.count(word) == 1:
                count += 1
        return count
    

#### OR
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count1, count2 = defaultdict(int), defaultdict(int)
        res = 0

        for word in words1:
            count1[word] +=1

        for word in words2:
            count2[word] +=1
            
        for word, count in count1.items():
            if count == 1 and count2[word] == 1:
                res += 1
                
        return res