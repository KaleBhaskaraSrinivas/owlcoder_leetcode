class Solution:
    def countPoints(self, rings: str) -> int:
         return sum([1 for i in range(10) if 'R'+str(i) in rings and 'G'+str(i) in rings and 'B'+str(i) in rings])
        
