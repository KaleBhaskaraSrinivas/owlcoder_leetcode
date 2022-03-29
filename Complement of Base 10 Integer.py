class Solution:
    def bitwiseComplement(self, n: int) -> int:
        s=0
        t=0
        if n==0:
            return 1
        while n:
            r=n%2
            n=n//2
            if r==0:
                s=s+(2**t)
            t=t+1
        return s
