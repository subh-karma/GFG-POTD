class Solution:
    def longestPath(self, mat, xs, ys, xd, yd):
        n = len(mat)
        m = len(mat[0])

        if mat[xs][ys] == 0 or mat[xd][yd] == 0:
            return -1

        visited = [[False] * m for _ in range(n)]
        self.ans = -1

        def dfs(x, y, dist):
            if x == xd and y == yd:
                self.ans = max(self.ans, dist)
                return

            visited[x][y] = True

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if (0 <= nx < n and 0 <= ny < m and
                        mat[nx][ny] == 1 and not visited[nx][ny]):
                    dfs(nx, ny, dist + 1)

            visited[x][y] = False

        dfs(xs, ys, 0)
        return self.ans
        # code here
        
