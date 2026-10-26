"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        new_graph = Node(node.val)
        visited_nodes = {node.val: new_graph}
        stack = [node]
        while stack:
            node_visiting = stack.pop()
            neighbors_new = []
            for neighboor in node_visiting.neighbors:
                if neighboor.val not in visited_nodes:
                    neighboor_new = Node(neighboor.val)
                    visited_nodes[neighboor.val] = neighboor_new
                    stack.append(neighboor)
                else:
                    neighboor_new = visited_nodes[neighboor.val]
                neighbors_new.append(neighboor_new)
            # Update neighboor list of new node:
            visited_nodes[node_visiting.val].neighbors = neighbors_new
        return new_graph