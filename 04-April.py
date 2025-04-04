
class Solution:
    def dfs(self, cur, prev, adj, vis):
        for i in adj[cur]:
            if i != prev and vis[i] == True:
                return True
                
            if i != prev:
                vis[i] = True
                res = self.dfs(i, cur, adj, vis)
                if res:
                    return True
                    
        return False
                
    
    def isCycle(self, V, edges):
        #Code here
        adj = [[] for i in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        vis = [False] * V
        vis[0] = True
        return self.dfs(0, -1, adj, vis)
