def is_proper(graph_set, color_set):
        for vertices in graph_set:
            for neighbors in graph_set[vertices]:
                if color_set[neighbors] == color_set[vertices]:
                    return False
        return True


def three_color(graph):
    vertex_list = []
    dictionario = {}
    generate_combinations(dictionario, graph, vertex_list, 0)
    return vertex_list


# Part of three_color - generates all possible combinations of three colors
def generate_combinations(dictionario, graph, list, depth):
    keys = []
    for key in graph:
        keys.append(key)
    keys.sort()
    if depth >= len(keys):
            list.append(dictionario)
    else:
        for x in range(1,4):
            dictionario[keys[depth]] = x
            generate_combinations(dictionario.copy(), graph, list, depth+1)


def is_three_color(graph):
    for vertex in graph:
        if len(graph[vertex]) >= 3:
            return False
    return True


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
            while matches_neighbor(graph, neighbor, coloring):
                coloring[neighbor] += 1
    return coloring



def matches_neighbor(graph, vertex, coloring):
    for neighbor in graph[vertex]:
        if coloring[vertex] == coloring[neighbor]:
            return True
    return False





print(is_proper({"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}, {"A": 1, "B": 2, "C": 3}))
print(three_color({"A": ["B"], "B": ["A"]}))
print(is_three_color({"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}),
      is_three_color({"A": ["B", "C", "D"], "B": ["A", "C", "D"], "C": ["A", "B", "D"], "D":["A", "B", "C"]}))
print(greedy({"A": ["B", "C"], "B": ["A"], "C": ["A"]}, ["A", "B", "C"]),
      greedy({"A": ["B"], "B": ["A", "C"], "C": ["B", "D"], "D": ["C"]}, ["A", "D", "B", "C"]))