class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for i in range(len(temperatures)):
            count = 1
            cur_temp = temperatures[i]
            for j in range(i+1, len(temperatures)):
                if cur_temp >= temperatures[j]:
                    count += 1
                else:
                    res.append(count)
                    break
            if len(res) <= i:
                res.append(0)
        
        return res



                    
        