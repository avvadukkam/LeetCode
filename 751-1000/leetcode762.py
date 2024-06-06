class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isPrime(num):
            if num > 1:
                for i in range(2, (num//2)+1):
                    if (num % i) == 0:
                        return False
                        break
                else:
                    return True
            else:
                return False
                
        primeCount = 0
        for i in range(left,right+1):
            if isPrime(bin(i).count('1')):
                primeCount +=1
        
        return primeCount