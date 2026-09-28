import math
class SegmentTree:
    def __init__(self, arr: list[int]):
        self.n = len(arr)
        # Allocate memory for the segment tree
        self.tree = [0] * (4 * self.n)
        if self.n > 0:
            self.build(arr, 0, 0, self.n - 1)
    def build(self, arr: list[int], node: int, start: int, end: int):
        if start == end:
            self.tree[node] = arr[start]
            return
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        self.build(arr, left_child, start, mid)
        self.build(arr, right_child, mid + 1, end)
        self.tree[node] = math.gcd(self.tree[left_child], self.tree[right_child])
    def update(self, node: int, start: int, end: int, idx: int, val: int):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        if start <= idx <= mid:
            self.update(left_child, start, mid, idx, val)
        else:
            self.update(right_child, mid + 1, end, idx, val)
        self.tree[node] = math.gcd(self.tree[left_child], self.tree[right_child])
    def query(self, node: int, start: int, end: int, l: int, r: int) -> int:
        # Range completely outside the segment
        if r < start or end < l:
            return 0
        # Range completely covers the segment
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        left_gcd = self.query(2 * node + 1, start, mid, l, r)
        right_gcd = self.query(2 * node + 2, mid + 1, end, l, r)
        return math.gcd(left_gcd, right_gcd)
class Solution:
    def processQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        if not arr:
            return []
        seg_tree = SegmentTree(arr)
        ans = []
        n = len(arr)
        for q in queries:
            if q[0] == 0:    # Type 1: Range GCD query [0, l, r]
                l, r = q[1], q[2]
                ans.append(seg_tree.query(0, 0, n - 1, l, r))
            elif q[0] == 1:  # Type 2: Point update query [1, index, value]
                idx, val = q[1], q[2]
                seg_tree.update(0, 0, n - 1, idx, val)
        return ans
        
