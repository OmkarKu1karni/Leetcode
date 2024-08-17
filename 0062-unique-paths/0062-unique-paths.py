def countpaths(i, j, n, m, dp):
    if i == n - 1 and j == m - 1:
        return 1
    if i >= n or j >= m:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = countpaths(i + 1, j, n, m, dp) + countpaths(i, j + 1, n, m, dp)
    return dp[i][j]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return countpaths(0, 0, m, n, dp)