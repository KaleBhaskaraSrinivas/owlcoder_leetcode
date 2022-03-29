class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        pr=[0 for i in range(len(nums))]
        pr[0]=nums[0]
        for i in range(1,len(nums)):
            pr[i]=pr[i-1]+nums[i]
        s=-1*(min(pr))+1
        if min(pr)>0:
            return 1
        return s
        
        
