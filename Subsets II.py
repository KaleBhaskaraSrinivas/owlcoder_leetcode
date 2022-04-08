class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[[]]
        for i in range(2**n):
            a=[]
            for j in range(n):
                if(i&(1<<j)):
                    a.append(nums[j])
                    a.sort()
            if(a not in ans and a[::-1] not in ans):
                ans.append(a)
        return(ans)
        
