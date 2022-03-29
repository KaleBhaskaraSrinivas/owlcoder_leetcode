class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        su, ans = 0, 0
        for i in range(len(nums)):
            su += nums[i]
            if su%k in d:
                ans += d[su%k]
            d[su%k] = d.get(su%k, 0) + 1
        return ans
    
   # d=dict()
     #   d={0:1}
      #      r=su%k
      #      if(r in d):
       #         ans+=d[r]
        #        d[r]+=1
         #   else:
          #      d[r]=1
        #return ans
     
            
                
