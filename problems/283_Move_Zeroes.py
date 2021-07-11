class Solution:
    def moveZeroes(self, nums) -> None:
        count = nums.count(0)
        for i in range(count):
            nums.remove(0)
            nums.append(0)

        # print(nums)

        # count = nums.count(0)
        # nums = list(filter(lambda x: x != 0, nums))
        # nums = nums.extend([0 for i in range(count)])

Solution().moveZeroes(nums=[0,1,0,3,12])