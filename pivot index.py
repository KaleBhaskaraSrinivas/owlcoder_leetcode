class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pr=[0 for i in range(len(nums))]
        pr[0]=nums[0]
        for i in range(1,len(nums)):
            pr[i]=pr[i-1]+nums[i]
        if pr[0]==pr[-1]:
            return 0
        for i in range(len(nums)-1):
            if pr[i+1]==pr[-1]-pr[i]:
                return i+1
        return -1
        
