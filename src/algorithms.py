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

    



                        