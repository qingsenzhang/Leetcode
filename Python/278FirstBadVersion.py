# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        
        start, end = 1, n
        while start + 1 < end:
            mid = (start + end) // 2
            if isBadVersion(mid) == True:
                end = mid
            else:
                start = mid
                
        if isBadVersion(start):
            return start
        else:
            return end
        
