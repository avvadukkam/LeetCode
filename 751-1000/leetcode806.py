class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        max_width = 100
        cur_width = 0
        lines = 1
        
        for char in s:
            char_width = widths[ord(char) - ord('a')]
            if cur_width + char_width > max_width:
                lines += 1
                cur_width = char_width
            else:
                cur_width += char_width
            
        return [lines, cur_width]