def is_proper(graph_set, color_set):
        for vertices in graph_set:
            for neighbors in graph_set[vertices]:
                if color_set[neighbors] == color_set[vertices]:
                    return False
        return True


def three_color(graph):
    vertex_list = []  # acts as return value to be operated on by helper
    dictionario = {}  # serves as a data structure for storing combinations
    generate_combinations(dictionario, graph, vertex_list, 0)  # recursive backtracer
    return vertex_list


# Part of three_color - generates all possible combinations of three colors
# This is recursive
def generate_combinations(dictionario, graph, vertex_list, depth):
    keys = []
    for key in graph:  # < == convert graph into a set of vertexes
        keys.append(key)
    keys.sort()  # <== maintains an order
    if depth >= len(keys):  # <== Base Case: depth is max depth
            vertex_list.append(dictionario)  # <== add the current dictionary to the final list
    else:                   # <== Not Base Case:
        for x in range(1,4):  # for each possible value 1, 2, and 3
            dictionario[keys[depth]] = x    # create a pathing with that value
            generate_combinations(dictionario.copy(), graph, vertex_list, depth+1)  # raise the depth for each path


# lazy method, just makes sure that each vertex has less than 3 edges
def is_three_color(graph):
    for vertex in graph:
        if len(graph[vertex]) >= 3:
            return False
    return True


# method to see if vertex connects to similarly colored vertex
def is_proper_edge(graph):
    for vertex in graph:
        colors_used = []
        for edges in graph[vertex]:
            if edges[1] in colors_used:
                return False
            else:
                colors_used.append(edges[1])
    return True


def greedy(graph, order):
    coloring = {}
    for x in order:
        coloring[x] = 1
    for vertex in order:
        for neighbor in graph[vertex]:
            coloring[neighbor] = 1
            while matches_neighbor(graph, neighbor, coloring):  # <== helper method that detects collisions
                coloring[neighbor] += 1
    return coloring


# helper method
def matches_neighbor(graph, vertex, coloring):
    for neighbor in graph[vertex]:  # <== for each neighbor
        if coloring[vertex] == coloring[neighbor]:  # if color matches
            return True  # report that housing violation
    return False    # if no reports filed, it must be good





print(is_proper({"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}, {"A": 1, "B": 2, "C": 3}))
print(three_color({"A": ["B"], "B": ["A"]}))
print(is_three_color({"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}),
      is_three_color({"A": ["B", "C", "D"], "B": ["A", "C", "D"], "C": ["A", "B", "D"], "D":["A", "B", "C"]}))
print(greedy({"A": ["B", "C"], "B": ["A"], "C": ["A"]}, ["A", "B", "C"]),
      greedy({"A": ["B"], "B": ["A", "C"], "C": ["B", "D"], "D": ["C"]}, ["A", "D", "B", "C"]))