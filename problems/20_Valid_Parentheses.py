# AC
class Solution:
    def isValid(self, s: str) -> bool:
        reference = {
            '{': '}',
            '[': ']',
            '(': ')',}
        stake = []
        for each in list(s):
            if each in ['{', '[', '(']:
                stake.append(each)
            elif not stake or each != reference[stake.pop()]:
                return False
        if len(stake) == 0:
            return True
        return False

print(Solution().isValid('()'))
