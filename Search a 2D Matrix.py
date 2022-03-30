class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[-1] >= target:
                return target in row
        return False
    
    
    
    #for i in range(len(matrix)):
    #for j in range(len(matrix[0])):
     #   if matrix[i][j]==target:
           # return True
#return False
        
