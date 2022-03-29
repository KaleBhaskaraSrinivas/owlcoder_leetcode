class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        p=0
        while 4**p<n:
            p+=1
        return 4**p==n
         
