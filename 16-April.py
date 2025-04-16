#User function template for Python

class Solution:
    def floydWarshall(self, dist):
        n = len(dist)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] != 10**8 and dist[k][j] != 10**8:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist

[k][j])#Code here
