class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        k = 0
        for i in range(len(typed)):
            if k < len(name) and typed[i] == name[k]:
                k+=1
            elif i == 0 or typed[i] != typed[i-1]:
                return False
        
        return k == len(name)