class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numset = set(nums)
        length = 0
        for num in numset:
            if num-1 not in numset:
                count = 1
                while num + count in numset:
                    count += 1
                length = max(length, count)
        return length
        