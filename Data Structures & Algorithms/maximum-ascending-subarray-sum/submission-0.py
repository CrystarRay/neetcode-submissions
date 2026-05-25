class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        listcounter = 0
        lastnum = 0
        counter = 0
        arr = []
        # nums = [10,20,30,5,10,50]
        # c = 30
        # lastnum = 10
        # 
        for i in nums:
            if lastnum >= i:
                arr.append(counter)
                counter = 0
            counter += i
            lastnum = i

            if listcounter == len(nums) - 1:
                arr.append(counter)
            listcounter += 1
            
        return max(arr)