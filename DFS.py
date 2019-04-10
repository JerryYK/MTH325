def find_par(tree, root, vert):
    if vert == root or vert not in tree:
        return []
    else:
        for item in tree:
            if vert in tree[item]:
                return item


def path(tree, root, vert):
    final_path = [vert]
    vertex = vert
    while vertex != root and vertex != []:
        vertex = find_par(tree, root, vertex)
        final_path.append(vertex)
    return final_path


def sub_tree(tree, root, vert):
    items = {}
    for item in tree:
        if vert in path(tree,root,item):
            items[vert] = tree[vert]
    return items


def pre_DFS(tree, root):
    items = [root]
    stack = [root]
    curr = 0
    while len(stack) > 0:
        curr = len(stack)-1
        for child in tree[stack[len(stack)-1]]:
            items.append(child)
            stack.append(child)
        stack.remove(stack[curr])
    return items



print(find_par({"A": ["B", "C"], "B":["D"], "C":[], "D":[]}, "A",  "D"),
      find_par({"A": ["B", "C"], "B":["D"], "C":[], "D":[]}, "A",  "A"))
print("path:",path({"A": ["B", "C"], "B":["D"], "C":[], "D":[]}, "A", "D"),
      path({"A": ["B", "C"], "B":["D"], "C":[], "D":[]}, "A",  "C"))
print(sub_tree({"A": ["B", "C"], "B":["D"], "C":[], "D":[]}, "A", "B"),
      sub_tree({"A": ["B", "C"], "B":["D"], "C":[], "D":[]}, "A",  "C"))
print("pre_dfs: ", pre_DFS({"A": ["B", "C"], "B":["D"], "C":[], "D":[]}, "A"),
      pre_DFS({"A": ["B", "C", "D"], "B":[], "C":[], "D":[]}, "A"))


