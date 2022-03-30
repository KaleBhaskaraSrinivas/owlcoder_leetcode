class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        dict={}
        for i in range(lowLimit, highLimit+1):
            total=0
            for j in str(i):
                total += int(j)
            if(total not in dict):
                 dict[total] = 0
            dict[total] += 1
        return max([dict[i] for i in dict])
        
