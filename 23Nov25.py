class Solution:
    def maxRemove(self, stones):
        from collections import defaultdict
        n = len(stones)
        parent = {}
        rank = defaultdict(int)
        
        def find(u):
            if u not in parent:
                parent[u] = u
            elif u != parent[u]:
                parent[u] = find(parent[u])
            return parent[u]
        
        def union(u, v):
            u, v = find(u), find(v)
            if u == v:
                return
            if rank[u] >= rank[v]:
                parent[v] = u
                if rank[u] == rank[v]:
                    rank[u] += 1
            else:
                parent[u] = v
        
        for x, y in stones:
            union(x, -y)
        return len(stones) - len(set(map(find, parent.keys())))
        # Code here
        
