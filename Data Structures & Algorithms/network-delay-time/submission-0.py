class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {}

        for time in times:
            u, v, t = time
            if u in adj_list:
                adj_list[u].append((v, t))
            else:
                adj_list[u] = [(v, t)]

        print(adj_list)

        dist = {node: float("inf") for node in range(1, n+1)}

        def dfs(t, node):
            if t >= dist[node]:
                return
            
            dist[node] = t

            if node in adj_list:
                for neighbor, time in adj_list[node]:
                    dfs(t+time, neighbor)

        dfs(0, k)
        res = max(dist.values())

        return res if res < float("inf") else -1
        


