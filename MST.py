def edge_get(graph):
    list_one = sort_edges(graph)
    list_two = []
    for item in list_one:
        list_two.append(item[1])
    return list_two


def sort_edges(graph):
    return_list = []
    for vertex in graph:
        for edge in graph[vertex]:
            if [edge[1], [edge[0], vertex]] in return_list:
                continue
            return_list.append([edge[1], [vertex, edge[0]]])
    return_list.sort()
    return return_list

def list_join(lst, elt1, elt2):
    main_list = lst
    merge_list_one = []
    merge_list_two = []
    for element in lst:
        if elt1 in element:
            merge_list_one = element
        else:
            if elt2 in element:
                merge_list_two = element
    if len(merge_list_one) == 0 or len(merge_list_two) == 0:
        return lst
    main_list.remove(merge_list_one)
    main_list.remove(merge_list_two)
    for items in merge_list_two:
        if items in merge_list_one:
            continue
        else:
            merge_list_one.append(items)
    main_list.append(merge_list_one)
    return main_list


def min_kruskal(graph):
    edges = edge_get(graph)
    final_answer = []
    chains = []
    for edge in edges:
        if in_chains(chains, edge) == [0, 0]:
            chains.append(edge)
            final_answer.append(edge.copy())
        else:
            if in_chains(chains, edge)[0] == 0 or in_chains(chains, edge)[1] == 0:
                final_answer.append(edge.copy())
                chains.append(edge.copy)
                list_join(chains, edge[0], edge[1])
            if in_chains(chains, edge)[0] != in_chains(chains, edge)[1]:
                final_answer.append(edge.copy())
                list_join(chains, edge[0], edge[1])
    return final_answer


def in_chains(chains, edge):
    position_dict = {edge[0]: 0, edge[1]: 0}
    for item in edge:
        counter = 0
        for chain in chains:
            if item in chain:
                counter += 1
                position_dict[item] = counter
            else:
                counter += 1
    return [position_dict[edge[0]], position_dict[edge[1]]]


def min_prim(graph, vertex):
    edges = edge_get(graph)
    chain = [vertex]
    vertex_set = [vertex]
    edge_set = []
    while len(vertex_set) < len(graph):
        for edge in edges:
            if in_chains(chain, edge)[0] != in_chains(chain, edge)[1]:
                if in_chains(chain, edge)[0] == 0 or in_chains(chain, edge)[1] == 0:
                    chain.append(edge.copy())
                    if edge[0] not in vertex_set:
                        vertex_set.append(edge[0])
                    if edge[1] not in vertex_set:
                        vertex_set.append(edge[1])
                    edge_set.append(edge.copy())
                    break
                continue
    return edge_set


def max_kruskal(graph):
    edges = edge_get(graph)[::-1]
    final_answer = []
    chains = []
    for edge in edges:
        if in_chains(chains, edge) == [0, 0]:
            chains.append(edge)
            final_answer.append(edge.copy())
        else:
            if in_chains(chains, edge)[0] == 0 or in_chains(chains, edge)[1] == 0:
                final_answer.append(edge.copy())
                chains.append(edge.copy)
                list_join(chains, edge[0], edge[1])
            if in_chains(chains, edge)[0] != in_chains(chains, edge)[1]:
                final_answer.append(edge.copy())
                list_join(chains, edge[0], edge[1])
    return final_answer


print("edge_get: ", edge_get({"A": [["B", 10], [ "D", 5]], "B": [["A", 10], ["C", 5]], "C": [["B", 5], ["D", 15]], "D": [["C",15 ],["A", 5 ]]}))
print("edge_get: ", edge_get({"V1": [["V2", 25], ["V9", 20], ["V10", 30]], "V2": [["V1", 25], ["V3", 10], ["V6", 5]], "V3": [["V2", 10], ["V4", 10], ["V8", 5]], "V4":[["V3", 10], ["V5", 5], ["V10", 5]], "V5":[["V4", 5], ["V6", 10], ["V9", 5]], "V6":[["V5", 10], ["V2",5], ["V7", 5]], "V7":[["V6", 5],["V8", 10], ["V10", 5]], "V8": [["V7", 10], ["V3", 5], ["V9", 15]], "V9":[["V1", 20], ["V5", 5],  ["V8", 15]], "V10":[["V1", 30], ["V4", 5], ["V7", 5]]}))

print("list_join: ", list_join([["A", "B"], ["C"], ["D"], ["E", "F"]], "A", "D"))
print("list_join: ", list_join([["A", "B"], ["C"], ["D"], ["E", "F"]], "A", "B"))

print("min_kruskal: ", min_kruskal({"A": [["B", 10], ["D", 5]], "B": [["A", 10], ["C", 5]], "C": [["B", 5], [ "D", 15]], "D": [["C", 15], ["A", 5]]}))
print("min_kruskal: ", min_kruskal({"A": [["B", 1], ["I", 5], ["H", 5]], "B": [["A", 1], ["C", 3], ["J", 4]], "C": [["B", 3], [ "D", 1], ["J", 4]], "D": [["C", 1], ["L", 3], ["E", 2]], "E" : [["D", 2], ["L", 3], ["F", 1]], "F" : [["E", 1], ["G", 5], ["K" , 2]], "G" : [["F", 5], ["K", 2], ["H", 1]], "H" : [["G", 1], ["I", 5], ["A" , 5]], "I" : [["A", 5], ["H", 5], ["K", 1],["J", 4]], "J" : [["I", 4], ["C", 4], ["L", 1], ["B", 4]], "L":[["J", 1], ["D", 3], ["K", 4], ["E", 3]], "K":[["G", 2], ["F", 2], ["L", 4], ["I", 1]]}))

print("min_prim: ", min_prim({"A": [["B", 10], [ "D", 5]], "B": [["A", 10], ["C", 5]], "C": [["B", 5], [ "D", 15]], "D": [["C",15 ], ["A", 5 ]]}, "A"))
print("min_prim: ", min_prim({"A": [["B", 1], ["I", 5], ["H", 5]], "B": [["A", 1], ["C", 3], ["J", 4]], "C": [["B", 3], [ "D", 1], ["J", 4]], "D": [["C", 1], ["L", 3], ["E", 2]], "E" : [["D", 2], ["L", 3], ["F", 1]], "F" : [["E", 1], ["G", 5], ["K" , 2]], "G" : [["F", 5], ["K", 2], ["H", 1]], "H" : [["G", 1], ["I", 5], ["A" , 5]], "I" : [["A", 5], ["H", 5], ["K", 1],["J", 4]], "J" : [["I", 4], ["C", 4], ["L", 1], ["B", 4]], "L":[["J", 1], ["D", 3], ["K", 4], ["E", 3]], "K":[["G", 2], ["F", 2], ["L", 4], ["I", 1]]}, "A"))

print("max_kruskal: ", max_kruskal({"A": [["B", 10], [ "D", 5]], "B": [["A", 10], ["C", 5]], "C": [["B", 5], [ "D", 15]], "D": [["C",15 ], ["A", 5 ]]}))
print("max_kruskal: ", max_kruskal({"A": [["B", 1], ["I", 5], ["H", 5]], "B": [["A", 1], ["C", 3], ["J", 4]], "C": [["B", 3], [ "D", 1], ["J", 4]], "D": [["C", 1], ["L", 3], ["E", 2]], "E" : [["D", 2], ["L", 3], ["F", 1]], "F" : [["E", 1], ["G", 5], ["K" , 2]], "G" : [["F", 5], ["K", 2], ["H", 1]], "H" : [["G", 1], ["I", 5], ["A" , 5]], "I" : [["A", 5], ["H", 5], ["K", 1],["J", 4]], "J" : [["I", 4], ["C", 4], ["L", 1], ["B", 4]], "L":[["J", 1], ["D", 3], ["K", 4], ["E", 3]], "K":[["G", 2], ["F", 2], ["L", 4], ["I", 1]]}))
