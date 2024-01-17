from euler import calculate_degrees, is_graph_connected

hamilton_test = [
    [0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0]
]


# our main function will be called recursively so number of vertices (-1) has to be outside, as well as initial list
num_vertices = len(hamilton_test)-1
hamilton = [0 for _ in range(num_vertices+1)]
is_criteria_checked = False


# we want this to be run once, that is why we have bool is_criteria_checked
def hamilton_criteria(graph):
    global is_criteria_checked
    # first part deals with criteria for Hamilton path/circuit
    is_criteria_checked = True
    if not is_graph_connected(graph):
        print("There is no Hamilton circuit nor Hamilton path")
        return
    no_circuit = False
    for degree in calculate_degrees(graph):
        if degree < 1:
            print("There is no Hamilton circuit nor Hamilton path")
            return
        elif degree < 2:
            print("There is no Hamilton circuit, but there may be Hamilton path")
            no_circuit = True
    if not no_circuit:
        print("There is a Hamilton circuit! (as well as Hamilton path)")


# backtracking algorithm implemented


def next_vertex(graph, index):
    while True:
        # chooses next vertex, prevents IndexError from happening, so we don't go over total number of vertices
        # and come back around
        hamilton[index] = (hamilton[index] + 1) % (num_vertices + 1)

        # if all vertices available to this index have been checked
        if hamilton[index] == 0:
            return
        # making sure the circuit does not form already, as we have to go through all vertices
        if index == 1:
            return
        j = 0
        # checking if there exists an edge between last chosen vertex and current vertex
        if graph[hamilton[index - 1]][hamilton[index]]:
            for i in range(1, index):
                j = i
                # if current vertex was chosen before, this is not valid for hamilton path
                if hamilton[i] == hamilton[index]:
                    break
            # only true if there were no breaks in the loop above, meaning vertex was not chosen before
            if j == index - 1:
                # checks if we are at the last vertex in the path
                if index < num_vertices or index == num_vertices:
                    # checks if there exists an edge between last vertex in the path and 1st vertex
                    # due to nature of checking previous vertex, the algotihm starts from 2nd vertex
                    if graph[hamilton[num_vertices]] [hamilton[1]]:
                        return


def hamilton_path_circuit(graph, index):
    # displays if hamilton criteria is met
    if not is_criteria_checked:
        hamilton_criteria(graph)
    while True:
        # finding the next valid vertex in the hamilton path/circuit
        next_vertex(graph, index)
        # if the value at the current index becomes 0, no more vertices can be added
        if hamilton[index] == 0:
            return
        # if at the last vertex in the path and there is an edge to the first vertex, we have the hamilton circuit
        if (index == num_vertices) and graph[hamilton[index]] [hamilton[1]]:
            hamilton.append(hamilton[1])
            print(hamilton[1:])
            hamilton.pop()
        else:
            # continue the search recursively with the next vertex
            hamilton_path_circuit(graph, index + 1)


hamilton_path_circuit(hamilton_test, 1)