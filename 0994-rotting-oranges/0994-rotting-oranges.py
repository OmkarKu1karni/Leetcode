class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                    vis[i][j] = 2
        delrow = [-1, 0, 1, 0]
        delcol = [0, 1, 0, -1]
        
        tm = 0
        while q:
            r, c, t = q.popleft()
            tm = max(tm, t)
            
            for i in range(4):
                nr = r + delrow[i]
                nc = c + delcol[i]
                
                if 0 <= nr < n and 0 <= nc < m and vis[nr][nc] != 2 and grid[nr][nc] == 1:
                    q.append((nr, nc, t + 1))
                    vis[nr][nc] = 2
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and vis[i][j] != 2:
                    return -1
        
        return tm