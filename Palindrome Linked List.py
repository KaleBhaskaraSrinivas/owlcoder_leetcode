class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s=''
        a = head
        while a:
            s += str(a.val)
            a = a.next 
        
        return True if s == s[::-1] else False
