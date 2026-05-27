class Solution:
    def wifiRange(self, s, x):
        max_gap = 2 * x
        # Starting with a gap of "x" because
        # we don't have a router to the left
        gap = x
        for c in s:
            if c == "0":
                gap += 1
                if gap > max_gap:
                    return False
            else:
                gap = 0
        # No router to the right so the max
        # "tail" gap can be only "x"
        return gap <= x
        # code here
