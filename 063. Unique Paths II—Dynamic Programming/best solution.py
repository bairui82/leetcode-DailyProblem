class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        if n == 0:
            return 0
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                else:
                    if i==0 and j==0:
                        res[i][j] = 1
                    else:
                        if i - 1 >= 0:
                            res[i][j] += res[i-1][j]
                        if j - 1 >= 0:
                            res[i][j] += res[i][j-1]
        return res[m-1][n-1]
