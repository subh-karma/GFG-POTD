class Solution:
    def __init__(self):
        self.stack = []
        self.content = ""
    def append(self, x):
        # append x into document
        self.content+=str(x)

    def undo(self):
        # undo last change
        if self.content:
            self.stack.append(self.content[-1])
            self.content = self.content[:-1]

    def redo(self):
        # redo changes
        if self.stack:
            self.content = self.content+self.stack.pop()
        

    def read(self):
        # read the document
        return self.content
