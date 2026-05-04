class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        last_pos_map = {}

        for i in range(len(s)):
            char = s[i]
            last_pos_map[char] = i

        i = 0
        while i<len(s):
            char = s[i]
            subs_len = last_pos_map[char] - i + 1

            j = 1
            while j < subs_len:
                subs_char = s[i+j]
                subs_len = max(last_pos_map[subs_char] - i + 1, subs_len)
                j += 1
            
            res.append(subs_len)
            i = subs_len + i
        
        return res



        

                
        