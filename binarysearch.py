class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        m=len(nums)-1
        
        while(l<=m):
            mid=l+(m-l)//2
            if (target==nums[mid]):
                return mid
            if(target>nums[mid]):
                l=mid+1
            else:
                m=mid-1
        return -1
                
                
