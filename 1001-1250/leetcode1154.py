class Solution:
    def dayOfYear(self, date: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year, month, day = map(int, date.split("-"))

        def isLeapYear(year):
            if year%4 == 0:
                if year%100 == 0:
                    if year%400 == 0:
                        return True
                    return False
                return True
            return False
            
        if isLeapYear(year):
            days[1] = 29
    
        return sum(days[:month-1]) + day