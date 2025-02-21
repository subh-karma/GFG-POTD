
class Solution:
    def isBalanced(self, st):
        stack = []
        for s in st:
            if s == "[" or s == "{" or s == "(":
                stack.append(s)
            elif stack and s == ")" and stack[-1] == "(":
                stack.pop()
            elif stack and s == "}" and stack[-1] == "{":
                stack.pop()
            elif stack and s == "]" and stack[-1] == "[":
                stack.pop()
            else:
                return False
        return not stack
            
                
