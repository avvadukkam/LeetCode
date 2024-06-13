class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        arr_len = len(arr)
        for piece in pieces:
            piece_len = len(piece)
            found = False
            for i in range(arr_len - piece_len + 1):
                if arr[i:i+piece_len] == piece:
                    found = True
                    break
            if not found:
                return False
        return True