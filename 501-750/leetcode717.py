class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        bits.reverse()
        while len(bits) > 2:
            if bits[-2:] in [[0,0],[0,1],[1,1]]:
                bits.pop()
                bits.pop()
            else:
                bits.pop()
        if bits == [0,1]:
            return False
        return True