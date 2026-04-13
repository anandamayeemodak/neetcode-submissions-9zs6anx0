class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.upper()
        
        for char in s:
            if 65 <= ord(char) <= 90 or 48 <= ord(char) <= 57:
                continue
            else:
                s = s.replace(char, "")

        left = 0
        right = len(s)-1

        while left<=right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False

        return True
        