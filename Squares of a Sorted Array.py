class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        square_elements = []
        for item in nums:
            prod = item*item
            square_elements.append(prod)
        square_elements.sort()
        return square_elements
        
