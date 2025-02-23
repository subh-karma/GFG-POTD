class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        # Initialize a stack to store elements for which we haven't found the next greater element
        stack = []
        # Initialize the result array with -1, which will be the default value if no next greater element is found
        result = [-1] * len(arr)
        
        # Traverse the array from right to left
        for i in range(len(arr) - 1, -1, -1):
            # Pop elements from the stack which are smaller than or equal to the current element
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            
            # If the stack is not empty, the top of the stack is the next greater element
            if stack:
                result[i] = stack[-1]
            
            # Push the current element onto the stack for future comparisons
            stack.append(arr[i])
        
        return result
