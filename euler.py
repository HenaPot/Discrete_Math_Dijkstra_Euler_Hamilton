
dijkstra_matrix = [
    [0, 6, 0, 1, 0],
    [6, 0, 5, 2, 2],
    [0, 5, 0, 0, 5],
    [1, 2, 0, 0, 1],
    [0, 2, 5, 1, 0]
]

simple_matrix = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

pendant_vertex_matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 1, 0, 0]
]

this_matrix_has_euler_circuit = [
    [0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 0],
    [1, 0, 1, 0, 0, 0]
]

no_euler_anything = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
]


def calculate_degrees(weighted_adjacency_matrix):
    adjacency_matrix = weighted_adjacency_matrix.copy()

    # we need to reset the adjacency matrix to 1s and 0s as other numbers don't represent the number of edges
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix)):
            if adjacency_matrix[i][j] > 0:
                adjacency_matrix[i][j] = 1

    # each row is one vertex, we just need to sum its edges
    degrees = [sum(row) for row in adjacency_matrix]
    return degrees


# we need all these arguments because of recursion
def depth_first_search(vertex, weighted_adjacency_matrix, visited_list):
    visited_list[vertex] = True
    for neighbor, edge in enumerate(weighted_adjacency_matrix[vertex]):
        if edge > 0 and not visited_list[neighbor]:
            depth_first_search(neighbor, weighted_adjacency_matrix, visited_list)


def is_graph_connected(weighted_adjacency_matrix):
    visited = [False for _ in weighted_adjacency_matrix]
    depth_first_search(0, weighted_adjacency_matrix, visited)
    return all(visited)


# works for connected multigraphs
def euler_path_circuit(weighted_adjacency_matrix):
    # the first part of this function deals with whether our graph meets the criteria for euler circuit
    only_euler_path = False
    euler_circuit = False
    odd_degree_vertices = []

    for vertex, degree in enumerate(calculate_degrees(weighted_adjacency_matrix)):
        if degree % 2 != 0:
            odd_degree_vertices.append(vertex)
    if len(odd_degree_vertices) > 2:
        print("There is no Euler circuit nor Euler path for this multigraph!")
        return None
    elif len(odd_degree_vertices) == 2:    # graph does not have to be strongly conneted in order to have euler path
        print("There is no Euler circuit, but there is Euler path for this multigraph!")
    elif len(odd_degree_vertices) == 0 and is_graph_connected(weighted_adjacency_matrix):
        print("There exists Euler circuit as well as Euler path for this multigraph!")
    else:
        print("There is no Euler circuit nor Euler path for this multigraph!")
        return None

    # here begins the algorithm for constructing euler circuits as given in the book (Fleury's algorithm)
    circuit = []
    # this is the H from the algorithm, edges will be removed as we go
    graph_copy = weighted_adjacency_matrix.copy()

    # runs for as many edges we have in H
    while any(edge for row in graph_copy for edge in row):
        subcircuit = []

        # if odd degree is present, that means we have euler path but not euler circuit
        start_vertex = odd_degree_vertices[0] if odd_degree_vertices else None

        # choosing the first vertex of non-zero degree to avoid isolated vertices without edges
        if start_vertex is None:
            for vertex, degree in enumerate(calculate_degrees(graph_copy)):
                if degree > 0:
                    start_vertex = vertex
                    break

        # runs until there are no more vertices with non-zero degrees
        while start_vertex is not None:
            subcircuit.append(start_vertex)
            next_vertex = None

            # all loops work with indexes in ascnending order so that first neighboring edge that exists
            # gets added to subcircuit. takes advantage of fact that euler circuit can start and end at any vertex
            for neighbor, edge in enumerate(graph_copy[start_vertex]):
                if edge > 0:
                    graph_copy[start_vertex][neighbor] -= graph_copy[start_vertex][neighbor]
                    graph_copy[neighbor][start_vertex] -= graph_copy[neighbor][start_vertex]
                    next_vertex = neighbor
                    break

            start_vertex = next_vertex

        circuit.extend(subcircuit)

    return circuit


#print(euler_path_circuit(dijkstra_matrix))








