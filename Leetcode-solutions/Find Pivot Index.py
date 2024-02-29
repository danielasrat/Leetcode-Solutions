class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)
        prefixsum = [0] * (n + 1)

        for i in range(1, n + 1):
            prefixsum[i] = prefixsum[i - 1] + nums[i - 1]

        for i in range(n):
            left_sum = prefixsum[i]
            right_sum = prefixsum[n] - prefixsum[i + 1]
            if left_sum == right_sum:
                return i

        return -1

t = Solution()
nums = [1, 2, 3]
print(t.pivotIndex(nums))
