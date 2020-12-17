# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def do_binary_search(self,low, high):
        mid = int(low + (high - low)/2)
        if(isBadVersion(mid)):
            if(isBadVersion(mid-1)):
                return self.do_binary_search(low, mid-1)
            else:
                return mid
        else:
            return self.do_binary_search(mid + 1, high)
        
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        low = 0
        high = n
        
        bad_version = self.do_binary_search(low, high)
        return bad_version
