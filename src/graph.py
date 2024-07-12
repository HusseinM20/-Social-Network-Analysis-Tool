class Graph:
    def __init__(self) :
        self.adjacency_list = {}

def add_vertex(self, vertex):
    if vertex not in self.adjacency_list:#to check if the vertex already exist or not
        self.adjacency_list[vertex] = {}

def add_edge(self, vertex1, vertex2):
    if  vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
def remove_vertex(self, vertex):
    if vertex in self.adjacency_list:
        self.adjacency_list.pop(vertex)
        for key, value in self.adjacency_list.items():
            if vertex in value:
                value.remove(vertex)
def remove_edge(self, vertex1, vertex2):
    if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
        if vertex2 in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].remove(vertex2)
            self.adjacency_list[vertex2].remove(vertex1)
def get_neighbors(self, node):
        return self.adjacency_list[node]  
def is_empty(self):
    return not bool(self.adjacency_list)
          

def display_graph(self):
    if self.adj_list == {}:
      print("Graph is empty!\n")
      return
    else:
        print("Vertices and their corresponding edges are:")
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex].keys())
        print("\n")
         
def __str__(self):
    return str(self.adjacency_list) 
def __len__(self):
    return len(self.adjacency_list)
def __contains__(self, vertex):
    return vertex in self.adjacency_list
def __getitem__(self, vertex):
    return self.adjacency_list[vertex]
