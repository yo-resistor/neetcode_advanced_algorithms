class UnionFind:
    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}
        
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, x: int) -> int:
        p = self.parent[x]
        
        while p != self.parent[p]:
            self.parent[x] = self.parent[p]
            p = self.parent[p]
        
        return p

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        p1, p2 = self.find(x), self.find(y)
        
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        
        return True

    def getNumComponents(self) -> int:
        disjoint = set()
        
        for i in self.parent:
            disjoint.add(self.find(i))
        
        return len(disjoint)

def main():
    union = UnionFind(10)
    
    print(union.isSameComponent(1, 3))
    print(union.union(1, 2))
    print(union.union(1, 3))
    print(union.getNumComponents())
    print(union.isSameComponent(1, 3))

if __name__ == "__main__":
    main()