class Graph:
    def __init__(self) :
        self.adjacency_list = {}

def add_vertex(self, vertex):
    if vertex not in self.adjacency_list:
        self.adjacency_list[vertex] = []
        print("Vertex", vertex, "has been added!\n")
    else:
        print("Vertex already exists")

def add_edge(self, vertex1, vertex2):
    if  vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            print("Edge between", vertex1, "and", vertex2, "has been added!\n")
    elif vertex1 not in self.adjacency_list and vertex2 not in self.adjacency_list:
      print("Vertex", vertex1, "and", vertex2, "do not exist")    
    elif vertex1 not in self.adjacency_list:
        print("Vertex", vertex1, "does not exist")
    else:
        print("Vertex", vertex2, "does not exist")    

