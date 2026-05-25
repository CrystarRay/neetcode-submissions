class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        curr = nums[0]
        res = curr

        for i in range(1, len(nums)):
            if not (nums[i-1] <nums[i]):
                curr = 0
            curr += nums[i]
            res = max(res, curr)
            
        return res