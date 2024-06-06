# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        ans = [[root.val]]
        queue = [root]
        flag = True

        while queue:
            temp = []
            q_len = len(queue)

            if flag:
                for _ in range(q_len):
                    if queue[0].right:
                        temp.append(queue[0].right.val)
                        queue.append(queue[0].right)
                    if queue[0].left:
                        temp.append(queue[0].left.val)
                        queue.append(queue[0].left)
                    
                    queue.pop(0)
    
                queue = queue[::-1]
                flag = False

            else:
                for _ in range(q_len):
                    if queue[0].left:
                        temp.append(queue[0].left.val)
                        queue.append(queue[0].left)
                    if queue[0].right:
                        temp.append(queue[0].right.val)
                        queue.append(queue[0].right)
                    
                    queue.pop(0)
    
                queue = queue[::-1]
                flag = True
            
            ans.append(temp)
        
        ans.pop()
        return ans
        