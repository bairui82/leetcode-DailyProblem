class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        
        mdp = [([0] * m) for i in range(n)]
        
        for i in range(n):
            for ii in range(m):
                if i==0 and ii == 0:
                    mdp[i][ii] = grid[i][ii]
                elif i == 0:
                    mdp[i][ii]=mdp[i][ii-1]+grid[i][ii]
                elif ii == 0:
                    mdp[i][ii]=mdp[i-1][ii]+grid[i][ii]
                else:
                    mdp[i][ii]=min(mdp[i-1][ii],mdp[i][ii-1])+grid[i][ii]
        return mdp[n-1][m-1]
