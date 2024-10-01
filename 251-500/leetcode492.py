# complex
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l = area
        w = 1
        dic = {l-w:[l,w]}
        minDiff = l-w
        while l>=w:
            w += 1
            l = int(area//w)
            minDiff = l-w
            if l*w==area and minDiff>=0:
                dic[l-w] = [l,w]
                
        return dic[min(dic)]
    
#easy
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for l in range(int(area**0.5), 0, -1):            
            if area % l == 0: 
                return [area // l, l]