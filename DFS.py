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


# This is just a wrapper for the recursive method below
def pre_DFS(tree, root):
    return pre_DFS_unWrapped(tree, root, root)


# This is the actual method for pre_DFS()
def pre_DFS_unWrapped(tree, root, vert):
    if len(tree[vert]) == 0:
        return vert
    else:
        ret = [vert]
        for child in tree[vert]:
            ret += pre_DFS_unWrapped(tree, root, child)
        return ret


# This is just a wrapper for the recursive method below
def post_DFS(tree, root):
    return post_DFS_unWrapped(tree, root, root)


# This is the actual method for post_DFS()
def post_DFS_unWrapped(tree, root, vert):
    if len(tree[vert]) == 0:
        return vert
    else:
        ret = []
        for child in tree[vert]:
            ret += pre_DFS_unWrapped(tree, root, child)
        ret += vert
        return ret


print(find_par({"A": ["B", "C"], "B":["D"], "C":[], "D":[]}, "A",  "D"),
      find_par({"A": ["B", "C"], "B":["D"], "C":[], "D":[]}, "A",  "A"))
print("path:",path({"A": ["B", "C"], "B":["D"], "C":[], "D":[]}, "A", "D"),
      path({"A": ["B", "C"], "B":["D"], "C":[], "D":[]}, "A",  "C"))
print(sub_tree({"A": ["B", "C"], "B":["D"], "C":[], "D":[]}, "A", "B"),
      sub_tree({"A": ["B", "C"], "B":["D"], "C":[], "D":[]}, "A",  "C"))
print("pre_dfs: ", pre_DFS({"A": ["B", "C"], "B":["D"], "C":[], "D":[]}, "A"),
      pre_DFS({"A": ["B", "C", "D"], "B":[], "C":[], "D":[]}, "A"))
print("post_dfs: ",post_DFS({"A": ["B", "C"], "B":["D"], "C":[], "D":[]}, "A"),
      post_DFS({"A": ["B", "C", "D"], "B":[], "C":[], "D":[]}, "A"))


