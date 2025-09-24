# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:

        self.output = []

        if not root:
            return self.output
        
        def is_leaf(node):
            return node and not node.left and not node.right

        def left_boundary(node):
            curr = node.left
            while curr:
                if not is_leaf(curr):
                    self.output.append(curr.val)
                if curr.left:
                    curr = curr.left
                else:
                    curr = curr.right
        
        def leaves(node):
            if node is None:
                return
            if is_leaf(node):
                self.output.append(node.val)
            else:
                leaves(node.left)
                leaves(node.right)

        def right_boundary_reversed(node):
            curr = node.right
            temp = []
            while curr:
                if not is_leaf(curr):
                    temp.append(curr.val)
                if curr.right:
                    curr = curr.right
                else:
                    curr = curr.left
            # add in reverse order
            self.output.extend(temp[::-1])
        
        if not is_leaf(root):
            self.output.append(root.val)
        left_boundary(root)
        leaves(root)
        right_boundary_reversed(root)
    
        return self.output