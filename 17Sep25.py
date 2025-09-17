class Solution:
    def decodedString(self, s):
        stack = []
        n = len(s)
        i = n-1
        while i>=0:
            if s[i].isnumeric():
                numeric = ''
                while s[i].isnumeric() and i>=0:
                    numeric+=s[i]
                    i-=1
                string = ''
                stack.pop(-1)
                while stack[-1]!=']':
                    string += stack.pop(-1)
                stack.pop(-1)
                stack.append(string*int(numeric[::-1]))
            else:
                stack.append(s[i])
                i-=1
        return ''.join(stack[::-1])
        # code here
