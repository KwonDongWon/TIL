class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            if target-num in nums[idx+1:]:
                return [idx, 1 + idx + nums[idx+1:].index(target-num)]
        