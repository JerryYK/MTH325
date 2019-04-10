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


print(edge_get({"A": [["B", 10], [ "D", 5]], "B": [["A", 10], ["C", 5]], "C": [["B", 5], ["D", 15]], "D": [["C",15 ],["A", 5 ]]}))
print(list_join([["A", "B"], ["C"], ["D"], ["E", "F"]], "A", "D"),
      list_join([["A", "B"], ["C"], ["D"], ["E", "F"]], "A", "B"))
print(min_kruskal({"A": [["B", 10], [ "D", 5]], "B": [["A", 10], ["C", 5]], "C": [["B", 5], [ "D", 15]], "D": [["C", 15], ["A", 5]]}))
print(min_prim({"A": [["B", 10], [ "D", 5]], "B": [["A", 10], ["C", 5]], "C": [["B", 5], [ "D", 15]], "D": [["C",15 ], ["A", 5 ]]}, "A"))