class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []

        for i in range(len(nums)-2):
            num_i = nums[i]
            for j in range(i+1, len(nums)-1):
                num_j = nums[j]
                two_sum = num_i + num_j
                
                if -two_sum in nums[j+1:]:
                    k = nums[j+1:].index(-two_sum) + j + 1
                    if sorted([num_i,num_j,nums[k]]) not in triplets:
                        triplets.append(sorted([num_i,num_j,nums[k]]))

        return triplets

        