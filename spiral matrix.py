class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        while len(matrix): 
            try: 
                ans+=matrix.pop(0) 
                ans+=[i.pop() for i in matrix] 
                ans+=matrix.pop()[::-1] 
                ans+=[i.pop(0) for i in matrix][::-1]
            except:
                break
        return ans
    
    
#Process would be repeated unless the length of matrix becomes zero.
# Exception handling, in case the pop operation on empty matrix is performed.
#Removing Top Row from matrix and inserting into answer list.
#Removing Rightmost Column from matrix and inserting into answer list.
#Removing Bottom Row from matrix and inserting into answer list in reverse order.
#Removing Leftmost Column from matrix and inserting into answers list in reverse order.
