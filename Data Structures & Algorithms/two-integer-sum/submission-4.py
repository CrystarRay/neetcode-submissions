class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sets = {} # val -> index
        for i, n in enumerate(nums):
            sets[n] = i
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in sets and sets[diff] != i:
                return [i, sets[diff]]
        return