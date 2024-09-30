#1
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dic = {}
        res = []
        for i in range(len(items1)):
            dic[items1[i][0]] = items1[i][1]
        for j in range(len(items2)):
            if items2[j][0] in dic:
                dic[items2[j][0]] += items2[j][1]
            else:
                dic[items2[j][0]] = items2[j][1]
        for k, v in dic.items():
            res.append([k,v])
            
        return sorted(res)
    
#2

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(int)
        for item, value in items1 + items2:
            dic[item] += value
            
        return sorted([i,v] for i, v in dic.items())
        