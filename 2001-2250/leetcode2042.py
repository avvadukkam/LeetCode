class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        max_num = 0
        for i in s.split():
            if i.isdigit():
                if int(i) > max_num:
                    max_num = int(i)
                else:
                    return False
        return True
