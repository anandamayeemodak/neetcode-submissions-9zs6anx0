class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        for i in range(n):
            visited = set()
            cur_gas = gas[i]
            j = i
            while cur_gas - cost[j] >= 0:
                if j in visited:
                    return j
                else:
                    visited.add(j)
                    cur_gas = cur_gas - cost[j]
                    j += 1
                    j = j%n
                    cur_gas = cur_gas + gas[j]

        return -1
                
            