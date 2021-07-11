class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        maxLen = 1
        curLen = 1
        curString = []
        inlistString = []
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                curLen = 1
                curString = []
                continue
            else:
                curLen += 1
                curString.append()
            if curLen > maxLen:
                maxLen = curLen
        return maxLen
                