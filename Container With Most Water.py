class Solution:
    def maxArea(self, height: List[int]) -> int:
        k=0
        i=0
        j=len(height)-1
        while(i<=j):
            s=min(height[i],height[j])*(j-i)
            if k<=s:
                k=s
            if height[j]>height[i]:
                i+=1
            else:
                j-=1
        return k
        
