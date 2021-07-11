import math
class Solution:
    def searchRange(self, nums, target: int):
        if not nums:
            return [-1, -1]

        left, right = 0, len(nums) - 1
        limit = math.log2(len(nums))
        bs_counter = 0
        while True:
            position = (left + right) // 2
            bs_counter += 1
            # print(f'bs_ctr:{bs_counter}, pos:{position}, nbr:{nums[position]}')
            if bs_counter > limit + 1:
                return [-1, -1]
            if nums[position] > target:
                right = position - 1
            elif nums[position] < target:
                left = position + 1
            elif nums[position] == target:
                # print(nums[position])
                break
        
        start_counter = 0
        start = end = position
        while True:
            # print(f'start_ctr:{start_counter}, pos:{start}, nbr:{nums[start]}')
            start_counter += 1
            if start - 1 >= 0 and nums[start-1] == nums[start]:
                start -= 1
            else:
                break
        end_counter = 0
        while True:
            # print(f'end_ctr:{end_counter}, pos:{end}, nbr:{nums[position]}')
            end_counter += 1
            if end + 1 < len(nums) and nums[end+1] == nums[end]:
                end += 1
            else:
                break
        # print(f'start:{start}, end:{end}')
        return [start, end]



result = Solution().searchRange(nums=[], target=0)
print(f'RESULT:{result}')