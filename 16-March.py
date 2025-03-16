
class Solution:
    def minJumps(self, arr):
        n = len(arr)
        # If there's only one element, no jumps are needed.
        if n == 1:
            return 0
        # If the first element is 0, we can't move anywhere.
        if arr[0] == 0:
            return -1
        
        # Initialize variables:
        # jumps: number of jumps required so far
        # maxReach: the farthest index that can be reached
        # step: steps we can still take in the current jump
        jumps = 1
        maxReach = arr[0]
        step = arr[0]
        
        # Traverse the array starting from index 1.
        for i in range(1, n):
            # If we have reached the end of the array, return the jump count.
            if i == n - 1:
                return jumps
            
            # Update the farthest index we can reach from here.
            maxReach = max(maxReach, i + arr[i])
            # Use a step to get to the current index.
            step -= 1
            
            # If no more steps remain, we must do another jump.
            if step == 0:
                jumps += 1
                # Check if the current position is at or beyond maxReach, meaning we are stuck.
                if i >= maxReach:
                    return -1
                # Reinitialize the steps to the amount we can take from current index.
                step = maxReach - i
                
        return -1


