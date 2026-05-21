class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([c.lower() if c.isalnum() else '' for c in s])
        for i in range(len(s)):
            if s[i] != s[-i-1]:
                return False
        return True