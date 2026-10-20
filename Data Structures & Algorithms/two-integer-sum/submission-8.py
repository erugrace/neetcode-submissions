class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = []
        for i,num in enumerate(nums):
            lst.append([num,i])
        lst.sort()
        left = 0
        right = len(lst) -1
        while left < right:
            nsum = lst[left][0] + lst[right][0]
            if nsum == target:
                return [min(lst[left][1], lst[right][1]), max(lst[left][1], lst[right][1])]
            elif nsum < target:
                left += 1
            else:
                right -= 1
        return []

            


        