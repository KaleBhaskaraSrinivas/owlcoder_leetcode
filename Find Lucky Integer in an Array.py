class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts=Counter(arr)

        print(counts.items())

        lucky=[elem for elem,frq in counts.items() if elem==frq ]

        

        return max(lucky) if lucky else -1

        
