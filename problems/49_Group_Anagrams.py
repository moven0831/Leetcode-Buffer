class Solution:
    def groupAnagrams(self, strs):
        ref = {}
        for i in range(len(strs)):
            this_tuple = tuple(sorted(strs[i]))
            if this_tuple not in ref:
                ref[this_tuple] = [strs[i]]
            else:
                ref[this_tuple].append(strs[i])
        return list((ref.values()))

print(Solution().groupAnagrams(strs=["eat","tea","tan","ate","nat","bat"]))