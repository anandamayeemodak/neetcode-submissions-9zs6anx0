"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        node_map = {}
        root = Node(val=node.val)
        node_map[node] = root


        def bfs(node):
            queue = deque([node])

            while queue:
                cur_node = queue.popleft()
                for n in cur_node.neighbors:
                    if n not in node_map:
                        node_map[n] = Node(n.val)
                        queue.append(n)
                    
                    node_map[cur_node].neighbors.append(node_map[n])
              

        
        bfs(node)
        return root