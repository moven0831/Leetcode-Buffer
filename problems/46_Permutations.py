class Solution:
    def permute(self, nums):
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [nums]
        else:
            lst = []
            for i in range(len(nums)):
                fixed = nums[i]
                varied = nums[:i] + nums[i+1:]
                varied_permutation = self.permute(varied)
                for p in varied_permutation:
                    lst.append([fixed]+p)
            return lst

this = Solution().permute(nums=[1,2,3,4,5])
print(this)