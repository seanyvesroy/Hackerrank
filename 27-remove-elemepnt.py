class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        count = 0
        while left <= right:
            if nums[left] == val and nums[right] != val:
                nums[left] = nums[right]
                nums[right] = val
                left += 1
                right -= 1
                count += 1
            elif nums[left] == val and nums[right] == val:
                right -= 1
                count += 1
            else:
                left += 1                    

        return len(nums) - count