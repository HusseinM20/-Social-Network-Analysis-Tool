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
def sort_users(self, attribute):
        def get_attribute(user):
            return getattr(user, attribute)
        self.users.sort(key=get_attribute)

def binary_search_user(self, attribute, value):
        self.sort_users(attribute)  # Ensure the list is sorted by the attribute
        left, right = 0, len(self.users) - 1
        while left <= right:
            mid = (left + right) // 2
            user_attribute_value = getattr(self.users[mid], attribute)
            if user_attribute_value == value:
                return self.users[mid]
            elif user_attribute_value < value:
                left = mid + 1
            else:
                right = mid - 1
        return None            

def merge_sort(arr, attribute):
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort each half
    left_half = merge_sort(left_half, attribute)
    right_half = merge_sort(right_half, attribute)
    
    # Merge the sorted halves
    sorted_arr = merge(left_half, right_half, attribute)
    return sorted_arr


 



                        