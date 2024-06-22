class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandie = max(candies)
        for i in range(len(candies)):
            candies[i] += extraCandies
            if candies[i] >= maxCandie:
                candies[i] = True
            else:
                candies[i] = False
        return candies