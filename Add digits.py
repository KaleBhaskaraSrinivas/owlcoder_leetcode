class Solution:
    def addDigits(self, num: int) -> int:
        s=0
        while num:
            r=num%10
            num//=10
            s+=r
            if num==0 and s>9:
                num=s
                s=0
        return s
