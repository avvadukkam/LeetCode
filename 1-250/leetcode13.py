class Solution:
    def romanToInt(self, s: str) -> int:
        rom_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum = 0
        for i in range(len(s)):
            if i!=len(s)-1 and rom_dict[s[i]] < rom_dict[s[i+1]]:
                sum -= rom_dict[s[i]]
            else:
                sum += rom_dict[s[i]]
        return sum