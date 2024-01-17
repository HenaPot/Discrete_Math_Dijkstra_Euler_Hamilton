
matrix = [
    [0, 6, 0, 1, 0],
    [6, 0, 5, 2, 2],
    [0, 5, 0, 0, 5],
    [1, 2, 0, 0, 1],
    [0, 2, 5, 1, 0]
]


def dijkstra_shortest_path(weighted_adjacency_matrix, start_vertex):
    visited_nodes = []
    # nodes are set from 0 to number of vertices - 1 instead of names
    unvisited_nodes = [i for i in range(len(weighted_adjacency_matrix))]
    shortest_path = []

    # defines initialization of dijkstra's shortest path algorithm
    for vertex in unvisited_nodes:
        if vertex == start_vertex:
            shortest_path.append([vertex, 0, "/"])
        else:
            shortest_path.append([vertex, float('inf'), "previous vertex"])

    # the algorithm keeps running until all vertices are visited
    while unvisited_nodes:
        # lambda arguments: expression, sort unvisited_nodes in ascending order based on link weight for that node
        unvisited_nodes.sort(key=lambda x: shortest_path[x][1])
        current_vertex = unvisited_nodes.pop(0)

        # loop because we need the shortest distance from start_vertex to every other, all edges should be checked
        for neighbor_vertex in range(len(weighted_adjacency_matrix)):
            # current_vertex is the row, neighbor vertex is column, 0 in adjacency matrix means no edge exists
            if weighted_adjacency_matrix[current_vertex][neighbor_vertex] > 0:

                # distance has to take into account weight all the way from the start vertex
                new_distance = shortest_path[current_vertex][1] + weighted_adjacency_matrix[current_vertex][neighbor_vertex]
                if new_distance < shortest_path[neighbor_vertex][1]:
                    shortest_path[neighbor_vertex][1] = new_distance
                    shortest_path[neighbor_vertex][2] = current_vertex

        visited_nodes.append(current_vertex)

    # considering vertices/nodes are usually represented by letters, translation for vertices is given
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']

    for record in shortest_path:
        # accounts for the fact that start_vertex record in the shortest_path will have record[2] = '/'
        try:
            print(f"Vertex {alphabet[record[0]]}: Distance from start = {record[1]}, Previous Vertex = {alphabet[record[2]]}")
        except TypeError:
            print(f"Vertex {alphabet[record[0]]}: Distance from start = {record[1]}, Previous Vertex = {record[2]}")


dijkstra_shortest_path(matrix, 0)



