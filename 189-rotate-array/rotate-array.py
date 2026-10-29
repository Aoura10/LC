class Solution:

    def rev(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp

            start = start + 1
            end = end - 1

    def rotate(self, nums, k):
        n = len(nums)

        if n == 0:
            return

        k = k % n

        self.rev(nums, 0, n - 1)
        self.rev(nums, 0, k - 1)
        self.rev(nums, k, n - 1)