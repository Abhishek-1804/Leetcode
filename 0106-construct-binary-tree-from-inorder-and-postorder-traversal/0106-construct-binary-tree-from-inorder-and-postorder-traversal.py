# class TreeNode:
# Definition for a binary tree node.
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        # purpose of inorder is to keep track of our left and right nodes, so we just need to track the indexes
        # our value are always popped from postorder, we decide left or right node based on values in inorder

        inorderidx = {v:i for i,v in enumerate(inorder)}

        def helper(l, r):
            if l > r:
                return None

            root = TreeNode(postorder.pop())
            idx = inorderidx[root.val]
            root.right = helper(idx+1, r)
            root.left = helper(l, idx-1)

            return root
        
        return helper(0, len(inorder) - 1)