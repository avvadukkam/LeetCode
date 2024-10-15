class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-','').upper()
        len_first = len(s) % k

        res = s[:len_first] if len_first != 0 else ''

        for i in range(len_first,len(s),k):
            if res:
                res += '-'
            res += s[i:i+k]
            
        return res