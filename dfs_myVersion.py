def find_par(tree, root, vert):
    for par, vertex in tree.items():
        if vert == root:
            return []
        if vert in vertex:
            return par
def path(tree, root, vert):
    result = []
    result.append(vert)
    if root == vert:
        return result
    while(vert != root):
        for par, vertex in tree.items():
            if vert in vertex:
                result.append(par)
                vert = par  
                pass
    return result

def sub_tree(tree, root, vert):
    result = {}
    leaves = []
    target = []
    for par, vertex in tree.items():
        if len(tree[par]) == 0:
            leaves.append(par)
        if vert in vertex:
            target.append(par)
    for leaf in leaves:
        temp = path(tree, root, leaf)
        if vert not in temp:
            for note in temp:
                if note not in target:
                    target.append(note)
                
    
    for goal in target:
        del tree[goal]
        
    if vert != root and root in tree.keys():
        del tree[root]
    return tree

def toButtom(tree, vertex):
    if len(tree[vertex]) == 0:
            return vertex

    else:
        return toButtom(tree,tree[vertex][0])

def pre_DFS(tree, root):
    result = []
    while(True):
        target = toButtom(tree, root)
        if target == root:
            break
        parent = find_par(tree, root, target)
        temp = path(tree, root,target)
        temp.reverse()
        for vertex in temp:
            if vertex not in result:
                result.append(vertex)
    
        tree[parent].remove(target)
     
    return result


def post_DFS(tree, root):
    result = []
    while(True):
        target = toButtom(tree, root)
        parent = find_par(tree, root, target)
        if target == root:
            break
        if target not in result:
            result.append(target)
    
        tree[parent].remove(target)
        result.append(root)
     
    return result

print("toButtom(A): ", toButtom({"A": ["B"], "B":["C","I"], "C":["D","E", "G"], "E":["H"], "D":[], "H":[], "G":[],"I":["J"], "J":["K", "L"], "K":[], "L":[]},"A"))
print("path(A -> E): ", path({"A": ["B"], "B":["C","I"], "C":["D", "E", "G"], "E":["H"], "D":[], "H":[], "G":[],"I":["J"], "J":["K", "L"], "K":[], "L":[]},"A", "E"))
print("find_par(E): ", find_par({"A": ["B"], "B":["C","I"], "C":["D", "E", "G"], "E":["H"], "D":[], "H":[], "G":[],"I":["J"], "J":["K", "L"], "K":[], "L":[]},"A", "E"))
print("sub_tree(C): ", sub_tree({"A": ["B"], "B":["C","I"], "C":["D", "E", "G"], "E":["H"], "D":[], "H":[], "G":[],"I":["J"], "J":["K", "L"], "K":[], "L":[]}, "A", "C"))
print("pre_DFS(A): ", pre_DFS({"A": ["B"], "B":["C","I"], "C":["D", "E", "G"], "E":["H"], "D":[], "H":[], "G":[],"I":["J"], "J":["K", "L"], "K":[], "L":[]}, "A"))
print("post_DFS(A): ", post_DFS({"A": ["B"], "B":["C","I"], "C":["D", "E", "G"], "E":["H"], "D":[], "H":[], "G":[],"I":["J"], "J":["K", "L"], "K":[], "L":[]}, "A"))


