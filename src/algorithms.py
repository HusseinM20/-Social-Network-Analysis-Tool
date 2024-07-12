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

def merge(left, right, attribute):
    sorted_arr = []
    left_idx, right_idx = 0, 0
    
    # Compare elements from left and right subarrays
    while left_idx < len(left) and right_idx < len(right):
        if getattr(left[left_idx], attribute) <= getattr(right[right_idx], attribute):
            sorted_arr.append(left[left_idx])
            left_idx += 1
        else:
            sorted_arr.append(right[right_idx])
            right_idx += 1
    
    # Append remaining elements
    while left_idx < len(left):
        sorted_arr.append(left[left_idx])
        left_idx += 1
    
    while right_idx < len(right):
        sorted_arr.append(right[right_idx])
        right_idx += 1
    
    return 

def dijkstraAlgorithm(self, source):
    # Create a set to store the shortest distance from source to each vertex
    distance = {vertex: float('inf') for vertex in self.graph}
    # Set the distance of the source vertex to 0
    distance[source] = 0
    # Create a dictionary to store the visited vertices
    visited = {}
    
    while True:
        # Find the vertex with the minimum distance that has not been visited
        min_distance = float('inf')
        min_vertex = None
        for vertex in distance:
            if vertex not in visited and distance[vertex] < min_distance:
                min_distance = distance[vertex]
                min_vertex = vertex
        
        # If all vertices have been visited or there are no more reachable vertices, break the loop
        if min_vertex is None:
            break
        
        # Mark the current vertex as visited
        visited[min_vertex] = True
        
        # Update the distances of the neighboring vertices
        for neighbor, weight in self.graph[min_vertex].items():
            new_distance = distance[min_vertex] + weight
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
    
    return distance

def average_number_of_friends(graph):
    total_friends = sum(len(neighbors) for neighbors in graph.adjacency_list.values())
    return total_friends / len(graph.nodes())

def recommend_friends(graph, user_id):
    recommendations = {}
    for neighbor in graph.get_neighbors(user_id):
        for potential_friend in graph.get_neighbors(neighbor):
            if potential_friend != user_id and potential_friend not in graph.get_neighbors(user_id):
                if potential_friend not in recommendations:
                    recommendations[potential_friend] = 0
                recommendations[potential_friend] += 1
    
    return sorted(recommendations, key=recommendations.get, reverse=True)


def network_density(graph):
    n = len(graph.nodes())
    e = len(graph.edges())
    if n <= 1:
        return 0
    return 2 * e / (n * (n - 1))

