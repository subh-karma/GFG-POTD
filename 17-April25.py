class Solution:
    def findMinCycle(self, V, edges):
        # code here
        INF = float('inf')
        dist = [[INF] * V for _ in range(V)]
        adj = [[INF] * V for _ in range(V)]

        # Step 1: Build adjacency matrix
        for u, v, w in edges:
            if w < adj[u][v]:  # keep minimum weight if multiple edges
                adj[u][v] = w
                adj[v][u] = w
                dist[u][v] = w
                dist[v][u] = w

        min_cycle = INF

        # Step 2: Floyd-Warshall with cycle detection
        for k in range(V):
            # Check for cycles through vertex k
            for i in range(k):
                for j in range(i):
                    if dist[i][j] != INF and adj[i][k] != INF and adj[k][j] != INF:
                        cycle_weight = dist[i][j] + adj[i][k] + adj[k][j]
                        min_cycle = min(min_cycle, cycle_weight)

            # Standard Floyd-Warshall update
            for i in range(V):
                for j in range(V):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        return min_cycle if min_cycle != INF else -1
        

        

