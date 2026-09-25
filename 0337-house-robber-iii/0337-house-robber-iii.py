# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def dfs(self, node: Optional[TreeNode]) -> List[int]:
        if not node: return [0, 0]

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        rob = node.val + left[1] + right[1]
        skip = max(left[0], left[1]) + max(right[0], right[1])

        return [rob, skip]

    def rob(self, root: Optional[TreeNode]) -> int:
        ans = self.dfs(root)
        return max(ans[0], ans[1])
        