class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right+1):
            num = i
            while num:
                num, digit = divmod(num, 10)
                if digit == 0 or i % digit:
                    break
            else:
                res.append(i)  
        return res
