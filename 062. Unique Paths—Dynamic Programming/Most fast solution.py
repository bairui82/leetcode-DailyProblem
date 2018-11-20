class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # C^(m-1)_(m+n-2)
        res = 1
        for i in range(m, m+n-1):
            res *= i
            res /= i-m+1
        return int(res)
