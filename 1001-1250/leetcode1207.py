class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = defaultdict(int)
        
        for num in arr:
            dic[num] += 1

        occurrences = set()
        for count in dic.values():
            if count in occurrences:
                return False
            occurrences.add(count)
        return True