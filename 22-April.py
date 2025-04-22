from functools import reduce

class Solution:
    def findUnique(self, arr):
        return reduce(lambda x, y: x^y, arr)
