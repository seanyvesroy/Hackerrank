class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMax = nums[0]
        totalMax = nums[0]
        if len(nums) < 2:
            return nums[0]
        for i in range(1, len(nums)):
            currMax = max(nums[i], nums[i] + currMax)

            if currMax > totalMax:
                totalMax = currMax
        
        return totalMax