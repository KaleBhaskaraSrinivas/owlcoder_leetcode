class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res=dividend/divisor
        if res>=(2**31):
            return int(res)-1
        else:
            return int(res)
        
        
        
        
        
        
        
        
#         if dividend==-2147483648 and divisor==-1:
#             return 2147483647
#         return (int(dividend/divisor))
        
