class Solution(object):
    def minSteps(self, n):
        f = 2
        factors = 0
        while f <= n:
            if not n%f:
                n//=f
                factors += f
            else:
                f+=1
