nums = [1, 2, 3, 3, 4, 5, 5]
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sets = set(nums)
        print(len(sets))
        if len(sets) == len(nums):
            return False
        else:
            return True