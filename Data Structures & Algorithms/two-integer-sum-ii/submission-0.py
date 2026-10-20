class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1
        while left < right:
            nsum  = numbers[left] + numbers[right]
            if nsum == target:
                return [left+1, right+1]
            elif nsum < target:
                left += 1
            else:
                right -= 1
        