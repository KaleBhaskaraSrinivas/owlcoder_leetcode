class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return dict(Counter(nums).most_common(k)).keys()
