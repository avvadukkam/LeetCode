class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key_dic = {}
        i = 97
        for c in key.replace(" ", ''):
            if c not in key_dic:
                key_dic[c] = chr(i)
                i += 1
        
        res = ""
        for c in message:
            if c in key_dic:
                res += key_dic[c]
            else:
                res += c
        return res
    
# Optimized
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key_dic = {}
        i = 97

        for c in key:
            if c != ' ' and c not in key_dic:
                key_dic[c] = chr(i)
                i += 1
        
        return ''.join(key_dic.get(c, c) for c in message)