class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = {}

        for s in strs:
            if str(sorted(s)) in freq_map:
                freq_map[str(sorted(s))].append(s)
            else:
                freq_map[str(sorted(s))] = [s]
        
        res = []

        for key in freq_map.keys():
            res.append(freq_map.get(key))
        
        return res

