class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [([1] * m) for i in range(n)]
        for i in range(n):
            for ii in range(m):
                if i == 0 or ii == 0:
                    dp[i][ii] = 1
                else:
                    dp[i][ii]=dp[i-1][ii]+dp[i][ii-1]
        return dp[n-1][m-1]
