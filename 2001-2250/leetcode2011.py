class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for op in operations:
            if '+' in op:
                x += 1
            else:
                x -= 1
        return x
    
# optimized
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(1 if '+' in op else -1 for op in operations)