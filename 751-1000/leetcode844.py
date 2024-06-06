class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1, t1 = "", ""
        for i in s:
            if i != '#':
                s1 += i
            else:
                s1 = s1[:-1]
        for i in t:
            if i != '#':
                t1 += i
            else:
                t1 = t1[:-1]

        return s1==t1
    

''' OR'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(string):
            result = []
            for char in string:
                if char != '#':
                    result.append(char)
                elif result:
                    result.pop()
            return ''.join(result)

        return process_string(s) == process_string(t)
