import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # n = len(position)
        # fleets = [0]*n
        # fleet_hr_map = {}
        # new_fleet = 0

        
        # for idx in range(n):
        #     hrs = math.ceil((target - position[idx])/speed[idx]) 
        #     if hrs in fleet_hr_map:
        #         fleets[idx] = fleet_hr_map[hrs]
        #     else:
        #         new_fleet += 1
        #         fleet_hr_map[hrs] = new_fleet
        #         fleets[idx] = new_fleet
        
        # res = len(set(fleets))
        # return res

        n = len(position)
        monotonic_stack = []
        position_hr_map = []

        for idx in range(n):
            hrs = (target - position[idx])/speed[idx]
            position_hr_map.append([position[idx], hrs])
        
        position_hr_map.sort(reverse=True)


        for idx in range(n):
            monotonic_stack.append(position_hr_map[idx])
            if len(monotonic_stack) >= 2 and monotonic_stack[-1][1] <= monotonic_stack[-2][1]:
                monotonic_stack.pop()
        
        return len(monotonic_stack)







