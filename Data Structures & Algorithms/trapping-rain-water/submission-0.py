class Solution:
    def trap(self, height: List[int]) -> int:
        max_area = 0

        for i in range(1, len(height)-1):
            cur_height = height[i]
            pre_height = 0
            post_height = 0


            for pre_i in range(0, i):
                if height[pre_i] > cur_height:
                    pre_height = max(pre_height, height[pre_i])
            
            for post_i in range(i+1, len(height)):
                if height[post_i] > cur_height:
                    post_height = max(post_height, height[post_i])

            print("cur_height: ", cur_height)
            print(pre_height)
            print(post_height)

            max_area = max_area + max((min(pre_height, post_height)-cur_height), 0)
            print("max_area: ", max_area)
            
            


        
        return max_area