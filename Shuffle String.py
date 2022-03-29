class Solution(object):
    def restoreString(self, s, indices):
        return "".join(y for x,y in sorted(zip(indices,s)))
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        
