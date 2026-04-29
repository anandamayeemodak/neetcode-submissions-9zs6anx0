class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {i:[] for i in range(len(points))}

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
            

        res= 0
        visited= set()

        minH = [(0, 0)]

        while len(visited) < len(points) and minH:
            cost, pt = heapq.heappop(minH)
            if pt in visited:
                continue
            
            res += cost
            visited.add(pt)

            for next_cost, next_pt in adj[pt]:
                if next_pt not in visited:
                    heapq.heappush(minH, (next_cost, next_pt))

        return res


