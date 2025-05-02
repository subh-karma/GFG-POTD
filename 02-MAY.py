class Solution:

    def findMaximum(self, arr):
        n = len(arr)
        if n < 3: return max(arr)
        if arr[0] > arr[1]: return arr[0]
        if arr[-1] > arr[-2]: return arr[-1]
        
        ilo = 0
        ihi = n - 2
        while ilo < ihi:
            imid = (ilo + ihi + 1) // 2
            if arr[imid] < arr[imid + 1]:
                ilo = imid
            else:
                ihi = imid - 1
        return arr[ilo + 1]
