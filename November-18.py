class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        n = len(arr)
        if d>n:
            d = d % n
        ans = arr[d:] + arr[0:d]
        for i in range(n):
            arr[i] = ans[i]
