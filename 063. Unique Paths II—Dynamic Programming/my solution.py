class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        obstacleGrid= obstacleGrid
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        
        dp = [([1] * m) for i in range(n)]
        for i in range(n):
            for ii in range(m):
                if obstacleGrid[i][ii] == 1:
                    dp[i][ii] = 0
                elif i == 0:
                    if dp[i][ii-1]==0:
                        dp[i][ii]=0
                    else:
                        dp[i][ii] = 1
                elif ii == 0:
                    if dp[i-1][ii]==0:
                        dp[i][ii]=0
                    else:
                        dp[i][ii] = 1
                else:
                    dp[i][ii]=dp[i-1][ii]+dp[i][ii-1]
        return dp[n-1][m-1]
