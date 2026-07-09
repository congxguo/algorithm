class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def longest_zigzag(root):
    ans = 0
    
    def dfs(node):
        nonlocal ans
        if not node:
            return -1, -1
        
        # the longest zigzag start from node.left for both directions
        left_left, left_right = dfs(node.left)
        right_left, right_right = dfs(node.right)
        
        # confirm the longest zigzag path for the current node based on the left and right child nodes zigzag result
        left_len = left_right + 1
        right_len = right_left + 1
        
        ans = max(ans, left_len, right_len)
        
        return left_len, right_len
    
    dfs(root)
    return ans
    

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.right = TreeNode(4)
root.left.right.left = TreeNode(5)
root.left.right.left.right = TreeNode(6)

root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)
print(f'{longest_zigzag(root)}')