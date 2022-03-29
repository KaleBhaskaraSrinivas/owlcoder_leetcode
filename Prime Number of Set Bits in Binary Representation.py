class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isprime(num):
            if num==1:
                return False
            s=int(math.sqrt(num))
            for i in range(2,s+1):
                if num%i==0:
                    return 0
            return 1
        rc=0
        for n in range(left,right+1):
            sbc=0
            while n:
                r=n%2
                n=n//2
                sbc+=r
            rc+=isprime(sbc)
        return rc
            
