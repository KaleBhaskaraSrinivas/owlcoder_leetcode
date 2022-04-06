class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans=0
        d={}
        for i, x in enumerate(arr): 
            ans += d.get(target - x, 0)
            for k in range(i):
                sm = arr[k] + arr[i]
                d[sm] = 1 + d.get(sm, 0)
        return ans%1000000007
