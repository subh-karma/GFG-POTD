class Solution:
    def rowWithMax1s(self, arr):
        max_ones = 0
        row_index = -1

        for i in range(len(arr)):
            ones = sum(arr[i])
            if ones > max_ones:
                max_ones = ones
                row_index = i

        return row_index


        # code here
