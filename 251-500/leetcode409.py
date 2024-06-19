class Solution:
    def longestPalindrome(self, s: str) -> int:
        temp = {}
        pal_length = 0
        odd_count = 0

        for i in s:
            temp[i] = temp.get(i, 0) + 1

        for count in temp.values():
            pal_length += count // 2 * 2
            if count % 2 != 0:
                odd_count = 1

        return pal_length + odd_count