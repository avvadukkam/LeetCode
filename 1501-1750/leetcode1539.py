class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num = 1
        count = 0
        while True:
            if num not in arr:
                count += 1
                if count == k:
                    return num
            num += 1


# OR we can do it with binary serach method:
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            missing = arr[mid] - (mid + 1)
            if missing < k:
                left = mid + 1
            else:
                right = mid - 1
        return left + k
