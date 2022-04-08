class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        self.k = k   
    def add(self, val: int) -> int:
        index = self.findIndex(val,0,len(self.nums)-1)
        self.nums.insert(index,val)
        return self.nums[-self.k]
    def findIndex(self,target,low,high) -> int:
        if low > high:
            return low
        mid = (low+high)//2
        if self.nums[mid] == target:
            return mid
        if target < self.nums[mid]:
            return self.findIndex(target,low,mid-1)
        if target > self.nums[mid]:
            return self.findIndex(target,mid+1,high)      
        
