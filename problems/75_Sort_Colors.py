class Solution:
    def sortColors(self, nums) -> None:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.insert(0, nums.pop(i))
            elif nums[i] == 2:
                nums.insert(len(nums)-1, nums.pop(i))
                nums.insert(i, '*')
        for i in range(nums.count('*')):
            nums.remove('*')
        
        """"This method to cancel '*' is permitted"""
        # nums = list(filter(lambda x: x != '*', nums))
        # print(nums)

        # count_zero = nums.count(0)
        # count_one = nums.count(1)
        # count_two = nums.count(2)
        
        # color_list = [0 for i in range(count_zero)]  + \
        #     [1 for i in range(count_one)] + \
        #     [2 for i in range(count_two)]

        # return color_list

result = Solution().sortColors(nums=[1,2,0])
print(result)