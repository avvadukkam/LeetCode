class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
    
        first_freq = next(iter(freq.values()))

        for value in freq.values():
            if value != first_freq:
                return False
        return True