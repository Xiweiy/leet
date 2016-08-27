##SOLUTION 1 ITERATE UNTIL SQRT(N)

class Solution(object):
    def countPrimes(self, n):
        from math import sqrt
        isPrime = [False]*2+[True]*(n-2)
        ceil = int(sqrt(n)) +1
        for p in range(2,ceil):
            if not isPrime[p]:
                continue
            test = p*p
            while test < n:
                isPrime[test] = False
                test += p
        return sum(isPrime)


##SOLUTION 2  SKIP ALL EVEN NUMBERS
class Solution(object):
    def countPrimes(self, n):
        from math import sqrt
        
        if n <3:
            return 0
        isPrime = [False]*2+[True]*(n-2)
        
        count = 1
        for p in range(3,n,2):
            if not isPrime[p]:
                continue
            
            count +=1
            test = p*p
            while test < n:
                isPrime[test] = False
                test += p
        return count
