class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        n1 = n
        count = 1
        while time != 0:
            while n1 == n:
                count += 1
                time -= 1
                if time == 0:
                    break
                if count == n:
                    n1 = 1
            while n1 == 1:
                count -= 1
                time -= 1
                if time == 0:
                    break
                if count == 1:
                    n1 = n
        return count
    
# OR
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle_length = 2 * (n - 1)
        effective_time = time % cycle_length

        if effective_time < n:
            return 1 + effective_time
        else:
            return 2 * n - 1 - effective_time