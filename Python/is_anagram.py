class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter
        s_set = Counter(s)
        t_set = Counter(t)
        return s_set == t_set

if __name__ == "__main__":
    print(Solution().isAnagram("ab", 'ba'))