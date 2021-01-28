"""
Simple graph implementation

{
    '0': {'1', '3'},
    '1': {'0'},
    '2': set(),
    '3': {'0'}
}

"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id in self.vertices:
            return 

        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:         # make sure both vertexes are in graph
            self.vertices[v1].add(v2)                           # pointing from v1 to v2
        else:
            raise IndexError('Vertex does not exist')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]                             # returns all neighbors of vert with the vertex_id passed in

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()                                                 # use a Queue for breadth first
        q.enqueue(starting_vertex)                                  # add 'current vert' to the queue
        visited = set()

        while q.size() > 0:
            current = q.dequeue()                                   # dequeue 'current vert' so we can work with it

            if current not in visited:                              # check to see if we have already been to the vert - if we haven't -->
                print(current)                                      # print 
                visited.add(current)                                # add current to visited

                for next_vert in self.get_neighbors(current):       # loop through all edges in the set to get the neighbors
                    q.enqueue(next_vert)                            # add next vert to end of queue to continue looping through graph

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()                                                 # use a Stack for depth first
        s.push(starting_vertex)
        visited = set()

        while s.size() > 0:                                           # continue looping until our stack is empty
            current = s.pop()                                       # Stack allows you to go all the way down to the bottom of the path

            if current not in visited:
                print(current)
                visited.add(current)

                for next_vert in self.get_neighbors(current):
                    s.push(next_vert)                               # adds vert to the front of the stack

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        print(starting_vertex)
        visited.add(starting_vertex)

        for neighbor in self.get_neighbors(starting_vertex):

            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()                                     # track nodes we have visited and interaction is complete

        while q.size() > 0:
            path = q.dequeue()
            current = path[-1]

            if current not in visited:

                if current == destination_vertex:
                    return path

                visited.add(current)

                for next_vert in self.get_neighbors(current):
                    new_path = list(path)
                    new_path.append(next_vert)
                    q.enqueue(new_path)     

        return None


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])                           # put starting vertex in [] becauase we want our stack to be a LIST of paths
        visited = set()

        while s.size() > 0:
            path = s.pop()                                  # starting vertex
            vert = path[-1]                                 # possible destination vertex

            if vert not in visited:

                if vert == destination_vertex:
                    return path
                
                visited.add(vert)

                for next_vert in self.get_neighbors(vert):
                    new_path = list(path)                   # add the path (as a list) we have so far to the new path  
                    new_path.append(next_vert)              # append next_vert and continue 
                    s.push(new_path)

        return None                                         # if the path does not exist, return none


    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = None): # default value of None - user doesn't have to pass in values for visited or path, when we recurse we can pass a value in and have something to use
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if not visited:                                      # if visited is None
            visited = set()
        
        if not path:                                        # if path is None
            path = []
        
        visited.add(starting_vertex)
        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path

        for child_vert in self.get_neighbors(starting_vertex):

            if child_vert not in visited:
                new_path = self.dfs_recursive(child_vert, destination_vertex, visited, path)

                if new_path:
                    return new_path

        return None    
        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
