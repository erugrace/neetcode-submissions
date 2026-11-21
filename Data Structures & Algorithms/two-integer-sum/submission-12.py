class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in complement:
                return [complement[nums[i]], i]
            complement[diff] = i



            


        