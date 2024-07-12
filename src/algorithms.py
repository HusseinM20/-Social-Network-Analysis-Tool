from graph import Graph

def bfs(self):  
    # Create a queue for BFS
    queue = []
    visited = [False] * (len(self.graph))
    # Mark the source node as visited and enqueue it
    queue.append(self.source)
    visited[self.source] = True
    while queue:
        # Dequeue a vertex from queue and print it
        s = queue.pop(0)
        print(s, end = " ")
        # Get all adjacent vertices of the dequeued vertex s
        # If an adjacent has not been visited, then mark it visited and enqueue it
        for i in self.graph[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

def dfs(self, v, visited):
    # Mark the current node as visited and print it
    visited[v] = True
    print(v, end = " ")
    # Recur for all the vertices adjacent to this vertex
    for i in self.graph[v]:
        if visited[i] == False:
            self.dfs(i, visited) 




                        