from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def level_of_max_sum(root):
    queue = deque()
    queue.append(root)
    cur_level = 1
    max_level = 1
    max_value = float('-inf')
    while queue:
        sum = 0
        for _ in range(0, len(queue)):
            node = queue.popleft()
            sum += node.value
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        if sum > max_value:
            max_value = sum
            max_level = cur_level
        print(f'sum={sum}, cur_level={cur_level}, max_level={max_level}')
    
        cur_level += 1

        
    return max_level
    

root = TreeNode(1)

root.left = TreeNode(7)
root.right = TreeNode(0)

root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)

print(f'{level_of_max_sum(root)}')
