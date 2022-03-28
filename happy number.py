class Solution:
    def isHappy(self, n: int) -> bool:
        res=0
        while n:
            r=n%10
            n=n//10
            res+=pow(r,2)
            if n==0 and (res>=10 or res==7):
                print(res,end=" ")
                n=res
                res=0
        return res==1
