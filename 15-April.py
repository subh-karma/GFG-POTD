#User function Template for python3

class Solution:
    def bellmanFord(self, V, edges, src):
        #code here
        INF = 10**8
        dist = [INF]*V
        dist[src] = 0
                    
        for _ in range(V-1):
            for u, v, w in edges:
                if dist[u] != INF and dist[v] > dist[u] + w:
                    dist[v] = dist[u]+w
       
        for u, v, w in edges:
            if dist[u] != INF and dist[v] > dist[u]+w:
                return [-1]
        return dist
            
