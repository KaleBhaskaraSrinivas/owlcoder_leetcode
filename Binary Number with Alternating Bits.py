class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        d=n%2
        n=n//2
        while n:
            r=n%2
            n=n//2
            if(r==d):
                return False
            d=r
        return True
