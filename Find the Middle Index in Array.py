class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left=0
        right=sum(nums)
        for i in range(len(nums)):
            x = nums[i]
            right -= x
            if left == right:
                return i
            left += x
        return -1
    
    
    
    class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pr=[0 for i in range(len(nums))]
        pr[0]=nums[0]
        if nums==pr:
            return 0
        for i in range(1,len(nums)):
            pr[i]=pr[i-1]+nums[i]
        #return pr[-1]
        if pr[0]==pr[-1]:
            return 0
        for i in range(len(pr)-1):
            if pr[i]==pr[-1]-pr[i+1]:
                    return i+1
        else:
            return -1
    
        
            
