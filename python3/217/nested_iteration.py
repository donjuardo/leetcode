# Algorithm/technique: nested iteration
# Time complexity:     O(n^2)
# Auxiliary space:     O(1)
# Optimal:             no

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n: int = len(nums)
        if n < 2:
            return False

        i: int
        j: int
        # enumerate does not allow the last item to be skipped without slicing,
        # which would require linear auxiliary space.
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True

        return False
