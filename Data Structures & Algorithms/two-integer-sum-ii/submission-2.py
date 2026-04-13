class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):
            num = numbers[i]

            if (target-num) in numbers[i:]:
                j = numbers[i:].index(target-num) + i + 1
                return [i+1, j]
            
            else:
                continue
                



        