# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currentsum):
            if not node :
                  return False
            currentsum += node.val
            if not node.left and not node.right:
                return currentsum == targetSum
            return(dfs(node.left, currentsum)or dfs(node.right, currentsum))
        return dfs(root,0)