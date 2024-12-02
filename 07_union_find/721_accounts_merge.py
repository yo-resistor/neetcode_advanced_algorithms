from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_index_hash = {}
        
        for index, items in enumerate(accounts):
        # items = [name, email1, email2, ...]
            for email in items[1:]:
                if email in email_index_hash:
                # if email already exists in the hash map, union the indexes
                    uf.union(email_index_hash[email], index)
                else:
                # if email doesn't exist in the hash map, map the email to the index
                    email_index_hash[email] = index
        
        # set a result hash map
        # {index: [email1, email2, ...]}
        result_dict = {}
        for email, index in email_index_hash.items():
            leader_index = uf.find(index)
            if leader_index in result_dict:
            # if the root index exists in the result hash, add the email to the email list
                result_dict[leader_index].append(email)
            else:
            # if not, create a new map
                result_dict[leader_index] = [email]

        result_list = []
        for index, emails in result_dict.items():
            name = accounts[index][0]
            result_list.append([name] + sorted(result_dict[index]))
        
        return result_list

class UnionFind:
    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}
        
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0
    
    def find(self, node: int) -> int:    
        # the parent is not the root
        if self.parent[node] != node:
            # path shortening
            self.parent[node] = self.find(self.parent[node])
        
        return self.parent[node]
    
    def union(self, node1: int, node2: int) -> bool:
        p1 = self.find(node1)
        p2 = self.find(node2)
        
        # if two nodes have same root, return False
        # union is not possible
        if p1 == p2:
            return False
        
        # compare ranks of two branches, merge smaller into bigger
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        
        return True

def main():
    sol = Solution()
    
    accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
                ["John","johnsmith@mail.com","john00@mail.com"],
                ["Mary","mary@mail.com"],
                ["John","johnnybravo@mail.com"]]
    print(sol.accountsMerge(accounts))

if __name__ == "__main__":
    main()