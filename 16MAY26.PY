class Solution:
    
    def findSmallest(self, arr):
        
        # Sort the array
        arr.sort()

        # Smallest positive number that cannot be formed
        res = 1

        for num in arr:

            # If current number is greater than res,
            # res cannot be formed
            if num > res:
                break

            # Extend reachable range
            res += num

        return res
        # code here
