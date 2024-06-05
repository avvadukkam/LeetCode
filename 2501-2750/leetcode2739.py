class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        fuel_used = 0
        while mainTank >= 5:
            fuel_used += 5
            mainTank -= 5
            if additionalTank > 0:
                mainTank += 1
                additionalTank -= 1
        fuel_used += mainTank
    
        return fuel_used * 10
    
'''
Optimized version of the above code:
def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
    fuel_used = 0
    while mainTank >= 5:
        fuel_used += 5
        mainTank -= 4 if additionalTank > 0 else 5
        additionalTank = max(0, additionalTank - 1)
    return (fuel_used + mainTank) * 10

'''