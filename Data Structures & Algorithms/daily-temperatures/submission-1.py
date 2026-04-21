#Initial approach - similar to sliding window/counter => Time O(n2)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []

        # for i in range(len(temperatures)):
        #     count = 1
        #     cur_temp = temperatures[i]
        #     for j in range(i+1, len(temperatures)):
        #         if cur_temp >= temperatures[j]:
        #             count += 1
        #         else:
        #             res.append(count)
        #             break
        #     if len(res) <= i:
        #         res.append(0)
        
        # return res

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                stack_idx, stack_temp = stack.pop()
                res[stack_idx] = idx - stack_idx
            stack.append((idx, temp))

        return res



        



                    
        