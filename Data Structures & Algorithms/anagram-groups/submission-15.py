class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst1 = sorted(s)
        lst2 = sorted(t)
        if lst1 == lst2:
            return True
        return False


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst2 = []
        i = 0

        while (i < len(strs)) :
            lst1 = [strs[i]]
            j = i + 1
            while j < len(strs):
                if self.isAnagram(strs[i], strs[j]) == True:
                    lst1.append(strs[j])
                    strs.pop(j)
                else:
                    j += 1
                
            
            i += 1
            lst2.append(lst1)  
        return lst2


        