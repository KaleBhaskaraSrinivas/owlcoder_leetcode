class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s,p=0,1
        while n:
            r=n%10
            n=n//10
            s=s+r
            p=p*r
        return p-s
