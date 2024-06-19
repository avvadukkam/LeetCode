class Solution:
    def findComplement(self, num: int) -> int:
        bin_num = str(bin(num))[2:]
        comp = ''
        for i in bin_num:
            if i=="0":
                comp += "1"
            else:
                comp += "0"
        return int(comp,2)