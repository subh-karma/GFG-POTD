#User function Template for python3


class Solution:

    def kthElement(self, a, b, k):
        elements = []
        for i in a:
            elements.append(i)
        for i in b:
            elements.append(i)
        elements.sort()
        return elements[k-1]

