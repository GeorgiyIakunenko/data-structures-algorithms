# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(root):
            if root is None: return [True, 0]

            left, right = dfs(root.left), dfs(root.right)

            is_balanced = left[0] and right[0] and abs(right[1] - left[1]) < 2

            return [is_balanced, 1 + max(right[1], left[1])]

        return dfs(root)[0]


# test cases:

print(Solution().isBalanced(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(3)), TreeNode(2))))

print(Solution().isBalanced(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))))





