class Solution(object):
    def countConsistentStrings(self, allowed, words):
        allowed = set(allowed)
        return sum(1 for word in words if not set(word) - allowed)
