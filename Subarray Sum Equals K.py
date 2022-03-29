class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s=0
        ans=0
        C=Counter()
        for num in nums: 
            C[s]+=1
            s+=num  
            ans+=C[s-k]
        return ans
