from collections import deque

class AdjGraph:
    def __init__(self):
        self.graph = dict()
    

    def is_edge_exists(self, u, v):
        for dst_vertex in self.graph[u]:
            if dst_vertex == v:
                return True

        return False


    def add_edge(self, u, v):
        if u not in self.graph.keys():
            self.graph[u] = [v]
        
        else:
            if self.is_edge_exists(u, v):
                return
            self.graph[u].append(v)

        if v not in self.graph.keys():
            self.graph[v] = []
    

    def bfs(self):
        # 1. select start vertex, let's use the first one in list
        # 2. add it to a queue
        # 3. iterator the elements in the queue, if the linked array contains other collected vertex, add them to the queue
        # 4. iterator until the queue is empty
        queue = deque()
        visited = set()
        if not self.graph:
            return
        
        start_vertex = list(self.graph.keys())[0]
        print(f'start_vertex={start_vertex}')
        queue.append(start_vertex)

        while queue:
            print(f'queue={queue}')
            cur_vertex = queue.popleft()
            print(f'vertex={cur_vertex}')
            for vertex in self.graph[cur_vertex]:
                print(f'visited={visited}')
                if vertex in visited:
                    continue
                visited.add(vertex)
                queue.append(vertex)
        
        return visited


    def dfs_start_from(self, vertex, visited):
        if vertex in visited:
            return
        print(f'visited={visited}')
        print(f'dfs: vertex={vertex}')
        visited.add(vertex)
        for cur_vertex in self.graph[vertex]:            
            self.dfs_start_from(cur_vertex, visited)


    def dfs(self):
        if not self.graph:
            return

        visited = set()
        for vertex in self.graph.keys():
            self.dfs_start_from(vertex, visited)


    def __str__(self):
        return f'{self.graph}'


    def is_connected(self):
        visited = self.bfs()
        if len(visited) < len(self.graph.keys()):
            return False
        
        return True



graph = AdjGraph()
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(1, 3)
graph.add_edge(4, 0)
print(f'{graph}')
graph.bfs()
graph.dfs()

print(f'is_connected={graph.is_connected()}')