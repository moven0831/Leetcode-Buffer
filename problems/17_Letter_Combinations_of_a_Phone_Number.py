class Solution:
    phone_references = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }

    def letterCombinations(self, digits: str):
        if not digits:
            return []
        current_references = []
        for i in range(len(digits)):
            current_references.append(self.phone_references[digits[i]])
        # print(current_references)
        combination = []
        if len(digits) == 1:
            return current_references[0]
        elif len(digits) == 2:
            for i in range(len(current_references[0])):
                this = current_references[0][i]
                for j in range(len(current_references[1])):
                    this += current_references[1][j]
                    combination.append(this)
                    this = this[:len(digits)-1]
        elif len(digits) == 3:
            for i in range(len(current_references[0])):
                this = current_references[0][i]
                for j in range(len(current_references[1])):
                    this += current_references[1][j]
                    for k in range(len(current_references[2])):
                        this += current_references[2][k]
                        combination.append(this)
                        this = this[:len(digits)-1]
                    this = this[:len(digits)-2]
        elif len(digits) == 4:
            for i in range(len(current_references[0])):
                this = current_references[0][i]
                for j in range(len(current_references[1])):
                    this += current_references[1][j]
                    for k in range(len(current_references[2])):
                        this += current_references[2][k]
                        for l in range(len(current_references[3])):
                            this += current_references[3][l]
                            combination.append(this)
                            this = this[:len(digits)-1]
                        this = this[:len(digits)-2]
                    this = this[:len(digits)-3]
        
        # print(combination, len(combination))
        return combination

Solution().letterCombinations(digits="2")