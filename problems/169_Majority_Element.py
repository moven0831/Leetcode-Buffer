class Solution:
    def majorityElement(self, nums) -> int:
        ref = {}
        for i in range(len(nums)):
            if nums[i] not in ref:
                ref[nums[i]] = 1
            else:
                ref[nums[i]] += 1
        max_val = max(ref.values())
        for key, value in ref.items():
            if value == max_val:
                return key

print(Solution().majorityElement([1, 2, 3, 4, 2, 2]))