class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(" ","").replace("-","")
        if len(number) < 4:
            return number
        elif len(number) == 4:
            return number[:2]+'-'+number[2:]
        k = len(number) % 3 or 3
        if k == 1:
            k = 4
        for i in range(len(number)-k,0,-3):
            number = number[:i]+'-'+number[i:]
        if '-' not in number[-4:]:
            number = number[:-2] + '-' + number[-2:]
        return number
    
# OR

class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(" ","").replace("-","")
        if len(number) < 4:
            return number
        
        formatted_number = ''
        remaining_digits = len(number)
        while remaining_digits > 4:
            formatted_number += number[:3] + '-'
            number = number[3:]
            remaining_digits -= 3
        if remaining_digits == 4:
            formatted_number += number[:2] + '-' + number[2:]
        else:
            formatted_number += number
        
        return formatted_number