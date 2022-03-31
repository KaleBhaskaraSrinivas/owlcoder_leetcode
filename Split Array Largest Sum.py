def bin_search(l,h,mid,arr,m):
        sumi=0
        cnt=1
        for i in arr:
            if(sumi+i<=mid):
                sumi+=i
            else:
                cnt+=1
                sumi=i
        return (cnt<=m)
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        h=0
        for i in nums:
            h+=i
        l=max(nums)
        while(l<=h):
            mid=(l+h)//2
            if(bin_search(l,h,mid,nums,m)):
                h=mid-1
            else:
                l=mid+1
        return l
