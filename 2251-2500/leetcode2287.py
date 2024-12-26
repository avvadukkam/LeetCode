class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_dic = Counter(s)
        target_dic = Counter(target)

        return min(s_dic[c] // target_dic[c] if c in s_dic else 0 for c in target)