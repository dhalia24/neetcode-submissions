class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst1 = sorted(s)
        lst2 = sorted(t)
        if lst1 == lst2:
            return True
        return False
        