class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        curr_minutes = int(current[:2])*60 + int(current[-2:])
        corr_minutes = int(correct[:2])*60 + int(correct[-2:])
        
        diff = corr_minutes - curr_minutes

        count = 0

        for step in [60, 15, 5, 1]:
            count += diff // step
            diff %= step

        return count