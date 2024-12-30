class Solution:
    def fillCups(self, amount: List[int]) -> int:
        time = 0
        
        while sum(amount) > 0:
            amount.sort(reverse=True)
            
            if amount[0] > 0:
                amount[0] -= 1

            if amount[1] > 0:
                amount[1] -= 1
         
            time += 1

        return time