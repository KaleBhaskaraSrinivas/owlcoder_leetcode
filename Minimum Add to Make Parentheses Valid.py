class Solution(object):
    def minAddToMakeValid(self, s):
        stack = []
        for i in s:
            if i == "(" or not stack:
                stack.append(i)
            elif i == ")" and stack[-1]== "(":
                stack.pop()
            else:
                stack.append(i)
        return len(stack)
