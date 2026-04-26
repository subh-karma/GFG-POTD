class Solution:
    def commonElements(self, a, b, c):
        i, j, k = 0, 0, 0
        ans = []

        while i < len(a) and j < len(b) and k < len(c):

            # If all are same
            if a[i] == b[j] == c[k]:
                # Avoid duplicates in answer
                if not ans or ans[-1] != a[i]:
                    ans.append(a[i])

                i += 1
                j += 1
                k += 1

            # Move the smallest element's pointer
            elif a[i] < b[j]:
                i += 1
            elif b[j] < c[k]:
                j += 1
            else:
                k += 1

        return ans
        # code here
