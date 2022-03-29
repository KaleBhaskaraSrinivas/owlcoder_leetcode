class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dict={}
        for i,n in enumerate(mat):
            dict[i]=sum(n)
        abc = sorted(dict, key = dict.get)
        return abc[:k]
        
