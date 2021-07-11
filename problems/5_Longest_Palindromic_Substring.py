class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if string is even, put special char in the middle for process sakes
        even = True if len(s) % 2 == 0 else False 
        if even:
            s = s[:len(s)//2] + '#' + s[len(s)//2:]

        # build table
        table = []
        for i in range(len(s)):
            temp = []
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    temp.append(1)
                else:
                    temp.append(0)
            table.append(temp)

        # if table[i][0] == talbe[i-n][0+2n]
        # one-sided palindrome part += 1
        max_length = 1
        max_substring = s[0]
        counter = 1
        for i in range(1, len(s)):
            try:
                while table[i-counter][2*counter] == 1:
                    counter += 1
            except:
                pass
            if 2 * (counter - 1) + 1 > max_length:
                max_length = 2 * (counter - 1) + 1
                if even and counter <= 2 and i == len(s) // 2 and s[len(s)//2] == '#':
                    max_substring = s[i-(counter-1):len(s)//2] + \
                        s[len(s)//2+1] + \
                        s[len(s)//2+1:i+(counter-1)+1]
                else:
                    max_substring = s[i-(counter-1):i+(counter-1)+1]
            counter = 1
        return max_substring.replace('#', '')

print(Solution().longestPalindrome(s='cbbd'))

                
          