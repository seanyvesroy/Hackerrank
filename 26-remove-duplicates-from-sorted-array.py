class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        count = 0
        i = 0

        while i + count < (len(nums) - 1):
            
            
            if nums[i] == nums[i + 1]:
         
                nums.pop(i)
                nums.append(0)
                count = count + 1
            else:
                i = i + 1
        return len(nums) - count 