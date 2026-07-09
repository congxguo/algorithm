class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def build_tree(level):
    if not level or level[0] is None:
        return None

    root = TreeNode(level[0])
    queue = [root]
    i = 1

    while queue and i < len(level):
        node = queue.pop(0)

        if i < len(level) and level[i] is not None:
            node.left = TreeNode(level[i])
            queue.append(node.left)
        i += 1

        if i < len(level) and level[i] is not None:
            node.right = TreeNode(level[i])
            queue.append(node.right)
        i += 1

    return root


def lca(root, p, q):
    # part1: when to stop
    if root is None or root == p or root == q:
        return root
    
    # part2: recursive call
    # for a node, given we find p before q
    # if q is in the subtree of p, we will definitely get a None value in the other travserse branch
    # if not, we will get 2 not None value
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    
    # part3: how to resolve the result of recursive
    # note the returned value is not necessary p or q, it could be the lca of them
    if left and right:
        return root
    return left if left else right


def find(root, value):
    if not root:
        return None
    if root.value == value:
        return root
    return find(root.left, value) or find(root.right, value)


level_order = [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1]
root = build_tree(level_order)

p = find(root, 1)   # first 1 encountered
q = find(root.right.right, 1)  # deeper 1

lca = lca(root, p, q)
print(lca.value)