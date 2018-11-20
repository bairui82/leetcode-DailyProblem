class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def permute(a):
            val = 1
            for i in range(a):
                val *= (i+1)        
            return val
        if m == 1 or n == 1:
            return 1
        else:
            return int(permute(m+n-2)/(permute(n-1)*permute(m-1)))
