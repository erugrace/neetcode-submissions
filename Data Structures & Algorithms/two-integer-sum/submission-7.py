class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # A = []
        # for i, num in enumerate(nums):
        #     A.append([num, i])

        # A.sort()
        # i, j = 0, len(nums) - 1
        # while i < j:
        #     cur = A[i][0] + A[j][0]
        #     if cur == target:
        #         return [min(A[i][1], A[j][1]),
        #                 max(A[i][1], A[j][1])]
        #     elif cur < target:
        #         i += 1
        #     else:
        #         j -= 1
        # return []
        lst = []
        for i,num in enumerate(nums):
            lst.append([num,i])
        lst.sort()
        left = 0
        right= len(nums) -1
        while left <right:
            sumN = lst[left][0] + lst[right][0]
            if sumN == target:
                return [min(lst[left][1], lst[right][1]), max(lst[left][1],         lst[right][1])]
            elif sumN > target:
                right -= 1
            else:
                left += 1
        return []

            


        