class Graph:

    def __init__(self):
        self.graph = {}

    # Add a vertex
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    # Add an edge
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    # Display the graph
    def display(self):
        for vertex in self.graph:
            print(vertex, "->", self.graph[vertex])

    # Delete an edge
    def delete_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)
            if vertex1 in self.graph[vertex2]:
                self.graph[vertex2].remove(vertex1)

    # Delete a vertex
    def delete_vertex(self, vertex):
        if vertex in self.graph:
            for v in self.graph:
                if vertex in self.graph[v]:
                    self.graph[v].remove(vertex)

            del self.graph[vertex]


# Main Program
g = Graph()

# Add vertices
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")

# Add edges
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")

# Display the graph
print("Initial Graph:")
g.display()

# Delete edge A-B
print("\nAfter deleting edge A-B:")
g.delete_edge("A", "B")
g.display()

# Delete vertex D
print("\nAfter deleting vertex D:")
g.delete_vertex("D")
g.display()