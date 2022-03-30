class Solution(object):
    def halvesAreAlike(self, s):
        vowels = set("aeiouAEIOU")
        cnt1 = cnt2 = 0
        left, right = 0, len(s)-1
        while left < right:
            cnt1 += s[left] in vowels
            cnt2 += s[right] in vowels
            left += 1
            right -= 1
        return cnt1 == cnt2
        """
