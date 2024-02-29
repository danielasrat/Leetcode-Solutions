class NumArray:
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.prefixsum = [0] * len(nums)
        self.prefixsum[0]=nums[0]
        i = 1
        n = len(nums)-1
        while i<=n:
            self.prefixsum[i] = self.prefixsum[i-1] + nums[i]
            i+=1
    def sumRange(self, left: int, right: int) -> int:
        return self.prefixsum[right] - (self.prefixsum[left - 1] if left > 0 else 0)

t = NumArray([2, 3, 4, 5, 6])
param1 = t.sumRange(2, 4)
print(param1)  # Output should be 15
