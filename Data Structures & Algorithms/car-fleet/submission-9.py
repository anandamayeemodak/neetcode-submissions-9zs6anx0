#Initial approach => create fleets array and calculate hrs for every car to reach target
                #    does not consider car merger

#Final approach => use monotonic stack (strictly increasing hrs) with a list of lists
                #  [pos, hrs] -> the moment current top_hrs < current top-1_hrs, pop top since it will be slowed down to speed of car ahead in position
                #  No need for while loop since we are going in reverse sorted order
                #  so the elements below are already considered and will not be merged
                   
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







