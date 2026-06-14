class dsu:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        
        
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        rank_root_x = self.rank[root_x]
        rank_root_y = self.rank[root_y]

        print(f'rank_root_x={rank_root_x}, rank_root_y={rank_root_y}')

        if rank_root_x > rank_root_y:
            self.parent[root_y] = root_x
        elif rank_root_x < rank_root_y:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        print(f'parent={self.parent}, rank={self.rank}')

    def find(self, x):
        print(f'x={x}, parent={self.parent}, rank={self.rank}')

        if self.parent[x] == x:
            return x
        
        root = self.find(self.parent[x])
        self.parent[x] = root

        return root

    
dsu = dsu(4)
dsu.parent = [0, 0, 1, 2]
dsu.rank = [3, 2, 1, 0]
dsu.find(3)
print(f'parent={dsu.parent}, rank={dsu.rank}')