class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        
        low = float('-inf')
        stack = [preorder[0]]

        for num in preorder[1:]:
            if low < num < stack[-1]:
                stack.append(num)
            elif num > stack[-1]:
                while stack and num > stack[-1]:
                    low = stack.pop()
                stack.append(num)
            else:
                return False
        
        return True