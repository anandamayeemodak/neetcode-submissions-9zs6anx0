class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_map = {}

        if len(s) != len(t):
            return False
        

        for char in s:
            if char in freq_map:
                continue
            else:
                freq_map[char] = s.count(char)

        for char in t:
            if char in freq_map and t.count(char) == freq_map[char]:

                continue
            else:
                return False
        
        return True
        