#Solution 1: Not optimized
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        r, c = [], []
        temp = m*n
        for i in ops:
            r.append(i[0])
            c.append(i[1])
            temp = min(min(r)*min(c),temp)
        return temp if temp!=0 else m*n

#Solution 2: Optimized version of Solution 1
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops)==0:
            return m*n
        rows, cols = [], []
        for r, c in ops:
            rows.append(r)
            cols.append(c)
        return min(rows)*min(cols)

#Solution 3: Without using arrays
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops)==0:
            return m*n
        rows, cols = m, n
        for r, c in ops:
            rows, cols= min(r,rows), min(c,cols)
        return rows*cols

#Solution 4: Optimized version of Solution 3
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m*n
        return min(r for r, _ in ops) * min(c for _, c in ops)