
class Solution:
    def decodedString(self, s):
        # code here
        stack=[]
        for i in s:
            if i!=']':
                stack.append(i)
            else:
                string=""
                while stack and stack[-1]!='[':
                    string=stack.pop()+string
                stack.pop()
                num=""
                while stack and stack[-1].isdigit():
                    num=stack.pop()+num
                stack.append(int(num) *string)
        return "".join(stack)
                
