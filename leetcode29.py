class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0  
        ans = 0
        sign = 1 if (dividend > 0 and divisor > 0 or dividend <0 and divisor < 0) else -1

        m = abs(dividend)
        n = abs(divisor)

        while (m-n)>=0:
            count=0
            while (m-(n<<1<<count))>=0:
                count+=1
            ans+=1<<count
            m-=n<<count
        
        answer = sign*ans
        if answer > 2**31 - 1:
            return 2**31 - 1
        elif answer <= -2**31:
            return -2**31
        else:
            return answer