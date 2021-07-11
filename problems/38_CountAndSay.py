# AC

class Solution:
    def countAndSay(self, n: int):
        sentence = '1'
        for time in range(n-1):
            current = 0
            sentence_buffer = ''
            for i in range(len(sentence)):
                if current > i:
                    continue
                continuous_counter = 0
                for j in range(len(sentence)):
                    if current + j == len(sentence) - 1:
                        continuous_counter += 1
                    elif current + j > len(sentence) - 1:
                        break
                    elif sentence[current+j] == sentence[current+j+1]:
                        continuous_counter += 1
                        continue
                    else:
                        continuous_counter += 1
                        break
                sentence_buffer += f'{str(continuous_counter)}{sentence[i]}'
                current += continuous_counter
            sentence = sentence_buffer
        return sentence

for k in range(30):
    print(Solution().countAndSay(k))