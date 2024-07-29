class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = sorted(list(set(arr)))  # Remove duplicates
        rank_map = {num: i + 1 for i, num in enumerate(temp)}
        return [rank_map[num] for num in arr]