class Solution:
    def reverseString(self, s: List[str]) -> None:
        x,y = 0, len(s)-1 
        while (x < y):
          s[x],s[y] = s[y],s[x]
          x = x+1
          y = y-1
         