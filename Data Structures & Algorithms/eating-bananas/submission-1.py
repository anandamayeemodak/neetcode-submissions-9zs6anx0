import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        pile_sum = sum(piles)
        k = float('inf')

        while l<=r:
            rate_m = (l+r)//2
            #calc h_m at rate_m
            #if h_m > h, move l = rate_m + 1 ==>need to increase rate
            #else h_m <= h, move r = rate_m - 1 ==> need to decrease rate and store min_h_m
            #return min_h_m

            cur_h = 0
            for pile in piles:
                cur_h += math.ceil(pile/rate_m)
            
            if cur_h > h:
                l = rate_m + 1
            else:
                k = min(k, rate_m)
                r = rate_m - 1

        return k






        