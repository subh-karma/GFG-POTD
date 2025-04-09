class Solution:
    def articulationPoints(self, V, edges):
        from collections import defaultdict
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        disc = [-1] * V
        low = [-1] * V
        parent = [-1] * V
        visited = [False] * V
        ap = set()
        time = [0]

        def dfs(u):
            visited[u] = True
            disc[u] = low[u] = time[0]
            time[0] += 1
            children = 0

            for v in adj[u]:
                if not visited[v]:
                    parent[v] = u
                    children += 1
                    dfs(v)
                    low[u] = min(low[u], low[v])
                    if parent[u] != -1 and low[v] >= disc[u]:
                        ap.add(u)
                    if parent[u] == -1 and children > 1:
                        ap.add(u)
                elif v != parent[u]:
                    low[u] = min(low[u], disc[v])
        for i in range(V):
            if not visited[i]:
                dfs(i)
        return sorted(ap) if ap else [-1]
