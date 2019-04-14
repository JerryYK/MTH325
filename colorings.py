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





print("is_proper: ", is_proper({"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}, {"A": 1, "B": 2, "C": 3}))
print("is_proper: ", is_proper({"V1": ["V2", "V9", "V10"], "V2": ["V1", "V3", "V6"], "V3": ["V2", "V4", "V8"], "V4":["V3", "V5", "V10"], "V5":["V4", "V6", "V9"], "V6":["V5", "V2", "V7"], "V7":["V6", "V8", "V10"], "V8": ["V7", "V3", "V9"], "V9":["V1", "V5", "V8"], "V10":["V1", "V4", "V7"]}, {"V1": 1, "V2": 2, "V3": 3, "V4": 1, "V5" : 2, "V6" : 3, "V7" : 1, "V8" : 2, "V9" : 3, "V10" : 2}))

print("three_color: ", three_color({"A": ["B"], "B": ["A"]}))


print("is_three_color: ", is_three_color({"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}))
print("is_three_color: ", is_three_color({"A": ["B", "C", "D"], "B": ["A", "C", "D"], "C": ["A", "B", "D"], "D":["A", "B", "C"]}))

print("is_proper_edge: ", is_proper_edge({"A":[["B", 1], ["C", 2]], "B": [["A", 1], ["C", 3]], "C": [["A", 2], ["B", 3]]}))
print("is_proper_edge: ", is_proper_edge({"A":[["B", 1], ["C", 2]], "B": [["A", 1], ["C", 2]], "C": [["A", 2], ["B", 2]]}))
print("is_proper_edge: ", is_proper_edge({"V1": [["V2", 1], ["V9", 2], ["V10", 3]], "V2": [["V1", 1], ["V3", 2], ["V6", 3]], "V3": [["V2", 2], ["V4", 1], ["V8", 3]], "V4":[["V3", 1], ["V5", 2], ["V10", 4]], "V5":[["V4", 2], ["V6", 1], ["V9", 3]], "V6":[["V5", 1], ["V2",3], ["V7", 4]], "V7":[["V6", 4],["V8", 2], ["V10", 1]], "V8": [["V7",2 ], ["V3", 3], ["V9", 1]], "V9":[["V1", 2], ["V5", 3],  ["V8", 1]], "V10":[["V1", 3], ["V4", 4], ["V7", 1]]}))

print("greedy: ", greedy({"A": ["B", "C"], "B": ["A"], "C": ["A"]}, ["A", "B", "C"]))
print("greedy: ", greedy({"A": ["B"], "B": ["A", "C"], "C": ["B", "D"], "D": ["C"]}, ["A", "D", "B", "C"]))
print("greedy: ", greedy({"V1": ["V2", "V9", "V10"], "V2": ["V1", "V3", "V6"], "V3": ["V2", "V4", "V8"], "V4":["V3", "V5", "V10"], "V5":["V4", "V6", "V9"], "V6":["V5", "V2", "V7"], "V7":["V6", "V8", "V10"], "V8": ["V7", "V3", "V9"], "V9":["V1", "V5", "V8"], "V10":["V1", "V4", "V7"]}, ['V1' , 'V4', 'V7', 'V2', 'V9', 'V10', 'V3' , 'V5', 'V6', 'V8']))
