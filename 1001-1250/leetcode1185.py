class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        if month < 3:
            month += 12
            year -= 1

        century = year // 100
        year = year % 100

        # Calculate the day of the week using Zeller's congruence
        w = (day + int((13 * (month + 1)) / 5) + year + int(year / 4) + int(century / 4) - 2 * century - 1) % 7
        
        return days[w]