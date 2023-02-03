class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        tstring = str(x)
        reverse = tstring[::-1]
        if tstring == reverse:
            return True
        else:
            return False
