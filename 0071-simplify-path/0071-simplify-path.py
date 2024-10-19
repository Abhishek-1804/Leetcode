class Solution:
    def simplifyPath(self, path: str) -> str:
        
        # Split the path by '/' and process each component
        stack = []
        for f in path.split('/'):
            if f == '' or f == '.':
                continue  # Ignore empty and current directory references ('.')
            elif f == '..':
                if stack:  # Pop only if there's something to go back to
                    stack.pop()
            else:
                stack.append(f)  # Add valid directory names
        
        # Join stack with '/' to form the simplified path
        return '/' + '/'.join(stack)
