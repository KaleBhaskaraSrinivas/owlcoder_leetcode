
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        
            # if tx == 0 or ty == 0:
            #      return False 
            # if tx == sx:
            #       return (ty - sy) >= 0 and (ty - sy) % tx == 0 
            # if ty == sy: 
            #       return (tx - sx) >= 0 and (tx - sx) % ty == 0 
            # if tx > ty:
            #     return self.reachingPoints(sx, sy, tx % ty, ty) 
            # if tx < ty:
            #     return self.reachingPoints(sx, sy, tx, ty % tx)
            
            
            
            
            while(sx<tx and sy<ty):
                if(ty>tx):
                    ty=ty%tx
                else:
                    tx=tx%ty
            if (ty==sy and sx<=tx and (tx-sx)%sy==0 or tx==sx and sy<=ty and (ty-sy)%sx==0):
                return True
            return False
