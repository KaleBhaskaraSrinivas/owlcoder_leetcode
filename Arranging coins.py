class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n < 0:
            raise ValueError('the input is invalid')
        if n == 0:
            return 0

        counter = 0
        row = 1
        while n - row >= 0:
            n -= row
            counter += 1
            row += 1

        return counter
        
