# translates graph into a set of weighted edges
def edge_get(graph):
    list_one = sort_edges(graph) # call helper method to sort edges by weight
    list_two = []
    for item in list_one:
        list_two.append(item[1]) # remove weights
    return list_two


# identical to edge_get(graph) but inserts in reverse order
def edge_get_reverse(graph):
    list_one = sort_edges(graph)
    list_two = []
    for item in list_one:
        list_two.insert(0, item[1])
    return list_two


# breaks weighted graph into weighted edges, in ascending order
def sort_edges(graph):
    return_list = []
    for vertex in graph:  # for each vertex in the graph
        for edge in graph[vertex]: # for each edge attached to that vertex
            if [edge[1], [edge[0], vertex]] in return_list:  # checks if backwards copy is already included
                continue
            return_list.append([edge[1], [vertex, edge[0]]])  # otherwise, add edge to return list
    return_list.sort()  # <== where the magic happens
    return return_list


# method to join all sublists possible
def list_join(lst, elt1, elt2):
    main_list = lst  # what will eventually be returned
    merge_list_one = []
    merge_list_two = []
    for element in lst:         # Cycle through sublists
        if elt1 in element:     # if target vertex 1 is in sublist
            merge_list_one = element    # set that list to first mergelist
        else:
            if elt2 in element:     # if target vertex 2 is in sublist
                merge_list_two = element    # set that list to the second mergelist
    if len(merge_list_one) == 0 or len(merge_list_two) == 0:  # if one or the other isn't found
        return lst  # return the unchanged list
    main_list.remove(merge_list_one)  # otherwise, remove both sublists
    main_list.remove(merge_list_two)
    for items in merge_list_two:      # combine both sublists
        if items in merge_list_one:   # skip items already in sublist one
            continue
        else:
            merge_list_one.insert(0, items)
    main_list.append(merge_list_one)    # add merged sublist back into the main list
    return main_list


def min_kruskal(graph):
    edges = edge_get(graph)  # ordered edges
    final_answer = []   # return value
    chains = []  # collection of chains of vertices already selected
    for edge in edges:          # cycle through all edges
        if in_chains(chains, edge) == [0, 0]:   # if both vertexes are not in any of the chains
            chains.append(edge)     # create a new chain
            final_answer.append(edge.copy())    # include edge in final edge selection
            list_join(chains, edge[0], edge[1])
        else:
            if in_chains(chains, edge)[0] == 0 or in_chains(chains, edge)[1] == 0:  # if only ONE vertex is in chains
                final_answer.append(edge.copy())  # include the edge in final edge selection
                chains.append(edge)    # add edge as a new chain
                list_join(chains, edge[0], edge[1])  # merge that chain with a parent chain
            if in_chains(chains, edge)[0] != in_chains(chains, edge)[1]:  # if both vertexes are present in diff chains
                final_answer.append(edge.copy())  # include edge in final edge selection
                list_join(chains, edge[0], edge[1])  # merge the two chains
    return final_answer


# Helper method to check if an edge has vertices in the current selection
def in_chains(chains, edge):
    position_dict = {edge[0]: 0, edge[1]: 0}  # vertex value defaults to zero
    for item in edge:   # ## for each vertex
        counter = 0     # <== positional value of chain (zero equals not found)
        for chain in chains:    # ### for each chain in the list
            if item in chain:   # #### if the vertex is in the chain
                counter += 1    # Raise the counter
                position_dict[item] = counter   # and store the value
            else:
                counter += 1  # #### otherwise just raise the value
    return [position_dict[edge[0]], position_dict[edge[1]]]
    """Returns a pair of values, one for each vertex.  0 means not found, X represents which chain it was found in"""


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


# This is really just min_kruskal
def max_kruskal(graph):
    edges = edge_get_reverse(graph)  # <== only difference is the use of reverse helper
    final_answer = []
    chains = []
    for edge in edges:
        if in_chains(chains, edge) == [0, 0]:
            chains.append(edge)
            final_answer.append(edge.copy())
        else:
            if in_chains(chains, edge)[0] == 0 or in_chains(chains, edge)[1] == 0:
                final_answer.append(edge.copy())
                chains.append(edge)
                list_join(chains, edge[0], edge[1])
            else:
                if in_chains(chains, edge)[0] != in_chains(chains, edge)[1]:
                    final_answer.append(edge.copy())
                    list_join(chains, edge[0], edge[1])
        list_join(chains, edge[1], edge[0])  # fixes formatting bugs?
    return final_answer


print(edge_get({"A": [["B", 10], [ "D", 5]], "B": [["A", 10], ["C", 5]], "C": [["B", 5], ["D", 15]], "D": [["C",15 ],["A", 5 ]]}))
print(list_join([["A", "B"], ["C"], ["D"], ["E", "F"]], "A", "D"),
      list_join([["A", "B"], ["C"], ["D"], ["E", "F"]], "A", "B"))
print("min_kruskal: ", min_kruskal({"A": [["B", 1], ["I", 5], ["H", 5]], "B": [["A", 1], ["C", 3], ["J", 4]], "C": [["B", 3], [ "D", 1], ["J", 4]], "D": [["C", 1], ["L", 3], ["E", 2]], "E" : [["D", 2], ["L", 3], ["F", 1]], "F" : [["E", 1], ["G", 5], ["K" , 2]], "G" : [["F", 5], ["K", 2], ["H", 1]], "H" : [["G", 1], ["I", 5], ["A" , 5]], "I" : [["A", 5], ["H", 5], ["K", 1],["J", 4]], "J" : [["I", 4], ["C", 4], ["L", 1], ["B", 4]], "L":[["J", 1], ["D", 3], ["K", 4], ["E", 3]], "K":[["G", 2], ["F", 2], ["L", 4], ["I", 1]]}))
print("min_kruskal: ", len(min_kruskal({"A": [["B", 1], ["I", 5], ["H", 5]], "B": [["A", 1], ["C", 3], ["J", 4]], "C": [["B", 3], [ "D", 1], ["J", 4]], "D": [["C", 1], ["L", 3], ["E", 2]], "E" : [["D", 2], ["L", 3], ["F", 1]], "F" : [["E", 1], ["G", 5], ["K" , 2]], "G" : [["F", 5], ["K", 2], ["H", 1]], "H" : [["G", 1], ["I", 5], ["A" , 5]], "I" : [["A", 5], ["H", 5], ["K", 1],["J", 4]], "J" : [["I", 4], ["C", 4], ["L", 1], ["B", 4]], "L":[["J", 1], ["D", 3], ["K", 4], ["E", 3]], "K":[["G", 2], ["F", 2], ["L", 4], ["I", 1]]})))
print("min kruskal: ", min_kruskal({"A": [["B", 10], [ "D", 5]], "B": [["A", 10], ["C", 5]], "C": [["B", 5], [ "D", 15]], "D": [["C", 15], ["A", 5]]}))
print(min_prim({"A": [["B", 10], [ "D", 5]], "B": [["A", 10], ["C", 5]], "C": [["B", 5], [ "D", 15]], "D": [["C",15 ], ["A", 5 ]]}, "A"))
print("max_kruskal: ", max_kruskal({"A": [["B", 1], ["I", 5], ["H", 5]], "B": [["A", 1], ["C", 3], ["J", 4]], "C": [["B", 3], [ "D", 1], ["J", 4]], "D": [["C", 1], ["L", 3], ["E", 2]], "E" : [["D", 2], ["L", 3], ["F", 1]], "F" : [["E", 1], ["G", 5], ["K" , 2]], "G" : [["F", 5], ["K", 2], ["H", 1]], "H" : [["G", 1], ["I", 5], ["A" , 5]], "I" : [["A", 5], ["H", 5], ["K", 1],["J", 4]], "J" : [["I", 4], ["C", 4], ["L", 1], ["B", 4]], "L":[["J", 1], ["D", 3], ["K", 4], ["E", 3]], "K":[["G", 2], ["F", 2], ["L", 4], ["I", 1]]}))

print("max_kurskal 2:", max_kruskal({"A": [["B", 10], [ "D", 5]], "B": [["A", 10], ["C", 5]], "C": [["B", 5], [ "D", 15]], "D": [["C", 15], ["A", 5]]}))
print("max_kruskal: ", max_kruskal({"A": [["B", 10], [ "D", 5]], "B": [["A", 10], ["C", 5]], "C": [["B", 5], [ "D", 15]], "D": [["C",15 ], ["A", 5 ]]}))
print("max_kruskal: ", max_kruskal({"A": [["B", 1], ["I", 5], ["H", 5]], "B": [["A", 1], ["C", 3], ["J", 4]], "C": [["B", 3], [ "D", 1], ["J", 4]], "D": [["C", 1], ["L", 3], ["E", 2]], "E" : [["D", 2], ["L", 3], ["F", 1]], "F" : [["E", 1], ["G", 5], ["K" , 2]], "G" : [["F", 5], ["K", 2], ["H", 1]], "H" : [["G", 1], ["I", 5], ["A" , 5]], "I" : [["A", 5], ["H", 5], ["K", 1],["J", 4]], "J" : [["I", 4], ["C", 4], ["L", 1], ["B", 4]], "L":[["J", 1], ["D", 3], ["K", 4], ["E", 3]], "K":[["G", 2], ["F", 2], ["L", 4], ["I", 1]]}))
print("max_kruskal: ", max_kruskal({"A": [["B", 10], [ "D", 5]], "B": [["A", 10], ["C", 5]], "C": [["B", 5], [ "D", 15]], "D": [["C",15 ], ["A", 5 ]]}))
print("max_kruskal: ", len(max_kruskal({"A": [["B", 1], ["I", 5], ["H", 5]], "B": [["A", 1], ["C", 3], ["J", 4]], "C": [["B", 3], [ "D", 1], ["J", 4]], "D": [["C", 1], ["L", 3], ["E", 2]], "E" : [["D", 2], ["L", 3], ["F", 1]], "F" : [["E", 1], ["G", 5], ["K" , 2]], "G" : [["F", 5], ["K", 2], ["H", 1]], "H" : [["G", 1], ["I", 5], ["A" , 5]], "I" : [["A", 5], ["H", 5], ["K", 1],["J", 4]], "J" : [["I", 4], ["C", 4], ["L", 1], ["B", 4]], "L":[["J", 1], ["D", 3], ["K", 4], ["E", 3]], "K":[["G", 2], ["F", 2], ["L", 4], ["I", 1]]})))