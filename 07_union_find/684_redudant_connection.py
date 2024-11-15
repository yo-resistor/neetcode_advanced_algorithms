from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}
        
        for i in range(1, n + 1):
            self.parent[i] = i
            self.rank[i] = 0
    
    # find the root node of a node
    def find_root(self, node: int) -> int:
        p = self.parent[node]
        
        while p != self.parent[p]:
            self.parent[node] = self.parent[p]
            p = self.parent[p]
        
        return p
    
    # union two nodes in a edge list by comparing ranks of two nodes
    # true: if union is possible and done
    # false: if union is not possible
    def union(self, node1: int, node2: int) -> bool:
        p1, p2 = self.find_root(node1), self.find_root(node2)
        
        # return false if the two nodes have same root
        if p1 == p2:
            return False
        
        # compare the rank of each node
        # add node with smaller rank to node with higher rank
        # if they have same ranks, add first to second node and increase the rank of the second node
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p2] < self.rank[p1]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        
        # return true after adding
        return True
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # initialize union tree using UnionFind class
        union_tree = UnionFind(len(edges))
        
        # go over each edge and union the nodes in the edge
        # if union function returns False, we have a cycle
        # return the edge that gives False
        for edge in edges:
            [node1, node2] = edge
            if not union_tree.union(node1, node2):
                return edge

def main():
    sol = Solution()
    
    edges = [[1,2],[1,3],[2,3]]
    print(sol.findRedundantConnection(edges))
    
    edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    print(sol.findRedundantConnection(edges))

if __name__ == "__main__":
    main()