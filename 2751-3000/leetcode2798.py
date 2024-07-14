class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        output = 0
        for ele in hours:
            if ele >= target:
                output += 1
        return output