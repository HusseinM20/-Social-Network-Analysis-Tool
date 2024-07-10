class Graph:
    def __init__(self) :
        self.adjacency_list = {}

def add_vertex(self, vertex):
    if vertex not in self.adjacency_list:
        self.adjacency_list[vertex] = {}
        print("Vertex", vertex, "has been added!\n")
    else:
        print("Vertex already exists")

def add_edge(self, vertex1, vertex2):
    if  vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            print("Edge between", vertex1, "and", vertex2, "has been added!\n")
    else:
            raise ValueError("Vertices must exist in the graph to add an edge.") 

def remove_vertex(self, vertex):
    if vertex in self.adjacency_list:
        self.adjacency_list.pop(vertex)
        for key, value in self.adjacency_list.items():
            if vertex in value:
                value.remove(vertex)
        print("Vertex", vertex, "has been removed!\n")
    else:
        print("Vertex does not exist in the graph!\n")

def remove_edge(self, vertex1, vertex2):
    if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
        if vertex2 in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].remove(vertex2)
            self.adjacency_list[vertex2].remove(vertex1)
            print("Edge between", vertex1, "and", vertex2, "has been removed!\n")
        else:
            print("No edge exists between", vertex1, "and", vertex2, "\n")
    else:
        print("Vertices must exist in the graph to remove an edge!\n")
        

def display_graph(self):
    if self.adj_list == {}:
      print("Graph is empty!\n")
      return
    else:
        print("Vertices and their corresponding edges are:")
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex].keys())
        print("\n")
         
