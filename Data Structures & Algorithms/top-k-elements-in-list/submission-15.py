class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        thisdict = {}
        set1 = set(nums)
        for elt in set1:
            thisdict.update({elt: 1})

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                thisdict[nums[i]] += 1

        sorted_dict = dict(sorted(thisdict.items(), key=lambda x: x[1], reverse = True))

        lst = []
        for x in sorted_dict.keys():
            if k > 0:
                lst.append(x)
                k -= 1
            else:
                break

        return lst
        