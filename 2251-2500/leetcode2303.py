class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        if income == 0:
            return 0

        tax = 0

        for i in range(len(brackets)):
            upper, percent = brackets[i]
            prev_upper = brackets[i-1][0] if i>0 else 0
            
            taxable = min(income, upper - prev_upper)
            tax += taxable * percent / 100
            income -= taxable
            
            if income <= 0:
                break
            
        return tax