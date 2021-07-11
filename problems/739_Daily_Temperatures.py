""" using stake to achieve O(2n)"""
class Solution:
    def dailyTemperatures(self, temperatures):
        """
        'Given a list of daily temperatures temperatures, return a list such that, 
        for each day in the input, tells you how many days you would have to wait
        until a warmer temperature.
        If there is no future day for which this is possible, put 0 instead.'

        Args:
            temperatures (List[int]): The list contained each day's temperature
        
        Returns:
            List[int]
        """
        
        waitday_list = [0] * len(temperatures)
        stack = []
        for index, val in enumerate(temperatures):
            # if stack has at least one element and
            # the top stack value is less than current value
            # (which implies the temp. become warmer)
            while stack and stack[-1][0] < val:
                # print(stack[-1][0])
                stack_top_index = stack.pop()[1]
                count = index - stack_top_index
                waitday_list[stack_top_index] = count
            stack.append((val, index))
        return waitday_list

result = Solution().dailyTemperatures(temperatures=[6,7,4,5,2,1])
# result = Solution().dailyTemperatures(temperatures=[34,34,47,47,34,34,34,47,34,47,47,47,34,34,34,47,47,34,47,47,34,34,34,34,47,34,34,47,34,34,34,47,47,47,47,47,47,34,34,34,47,34,34,47,34,47,47,47,34,47,47,34,47,34,47,47,34,47,47,34,34,47,47,47,34,34,47,47,47,34,34,47,34,34,34,47,47,34,34,47,47,47,47,47,34,34,34,47,47,34,47,34,47,34,34,47,34,47,47,47,47,47,47,34,34,34,47,34,47,34,47,34,34,34,34,47,34,34,34,34,34,34,34,47,34,34,47,47,34,47,47,47,47,47,47,47,34,34,47,34,47,34,47,34,34,34,47,34,34,47,34,47,47,34,47,47,47,47,34,34,34,34,47,47,34,34,34,47,34,34,47,34,34,47,34,34,34,34,47,34,34,34,47,34,34,47,47,34,47,47,34,34,34,34,34,34,47,47,34,47,34,47,34,47,47,47,34,47,34,34,34,34,34,47,47,47,47,47,47,34,47,34,47,34,34,34,47,47,47,34,47,47,34,47,47,47,34,47,47,34,47,47,34,47,34,34,47,47,34,34,34,34,47,34,34,47,47,34,47,47,34,34,34,34,47,47,34,34,47,47,34,47,34,47,34,47,47,47,47,34,34,47,47,34,34,34,47,34,47,47,47,34,47,47,34,34,34,34,34,47,47,34,47,47,34,34,47,34,47,47,34,47,47,47,47,47,47,47,34,34,34,34,47,47,34,47,34,47,47,34,47,47,34,34,34,47,47,47,34,47,34,47,47,47,34,34,34,34,34,34,34,47,34,34,34,34,47,47,34,34,47,34,47,47,34,47,34,34,47,47,47,47,47,47,34,34,47,34,34,47,34,47,47,47,47,47,34,34,34,47,47,34,47,34,34,47,47,47,34,34,47,47,47,34,34,47,47,34,34,47,47,47,47,34,34,34,47,34,34,47,47,34,34,34,47,34,34,47,34,34,34,34,47,34,47,34,47,47,47,34,34,47,47,47,47,47,34,47,34,34,34,34,34,47,47,34,34,47,47,34,34,47,34,47,34,47,34,47,47,47,47,47,47,47,47,47,34,47,47,47,34,47,47,34,34,47,34,47,34,34,47,47,47,47,34,47,34,34,34,47,47,47,34,34,47,47,34,34,34,34,47,47,34,47,34,34,47,47,34,47,34,47,34,47,34,34,47,34,47,34,47,34,47,47,47,47,47,34,34,47,47,34,34,34,47,34,34,34,34,34,47,47,47,34,47,47,47,47,47,47,47,47,34,34,34,34,47,34,47,34,47,47,47,34,34,34,34,47,34,47,34,47,34,47,34,34,34,47,34,47,34,34,47,34,34,47,34,34,47,47,47,34,47,47,47,34,34,34,34,34,34,34,47,34,34,47,34,47,34,47,34,34,34,34,47,47,47,47,34,47,34,34,34,47,34,47,47,47,34,34,47,34,47,47,34,47,34,34,34,47,34,34,34,47,34,34,34,34,34,34,47,47,47,47,34,47,47,34,47,34,47,34,47,34,47,34,34,47,34,47,34,47,34,34,34,34,34,47,47,47,47,47,47,47,47,47,34,47,47,34,34,34,47,34,34,47,47,34,47,47,47,47,47,47,47,34,47,34,47,47,47,47,47,47,34,47,47,34,34,34,47,47,47,47,34,34,47,47,34,34,34,34,34,47,34,34,34,34,47,47,34,47,47,47,47,47,47,47,34,34,47,34,47,34,47,47,47,47,34,47,47,47,34,34,34,34,34,34,47,47,47,34,34,34,47,47,34,47,34,47,47,47,34,47,47,47,47,47,47,47,34,47,47,47,34,34,47,47,34,47,47,34,34,34,47,34,47,34,34,47,34,47,34,34,34,34,47,47,47,34,47,34,47,47,34,47,34,47,34,47,34,47,47,47,34,34,47,34,47,34,47,47,47,47,47,34,47,34,47,34,47,34,34,47,47,47,47,47,34,47,34,47,47,47,47,47,47,47,34,47,47,47,34,34,34,47,34,47,47,47,47,34,47,47,34,47,34,34,47,47,34,34,47,34,47,47,47,47,34,47,47,34,34,34,47,47,34,34,47,34,47,34,47,34,47,47,47,47,34,47,47,34,34,34,47,34,47,34,47,34,34,34,47,34,34,34,34,34,34,47,47,47,34,47,47,47,34,34,34,34,47,34,34,47,34,34,47,47,34,34,47,34,34,47,34,34,47,34,47,47,34,47,47,34,34,47,47,34,34,47,34,34,47,47,34,47,34,34,47,47,47,34,34,47,47,34,34,34,47,47,34,47,34,47,47,34,34,34,47,47,47,47,34,47,47,34,47,47,34,47,34,47,34,47,47,34,34,47,47,47,34,47,47,47,34,34,34,47,47,47,47,34,47,47,34,34,34,34,34,34,34,34,47,34,47,47,34,47,47,34,47,47,47,47,47,34,47,34,34,34,34,47,47,47,47,34,34,34,47,34,34,34,47,47,34,47,47,34,47,34,34,34,47,34,47,47,47,34,34,34,34,47,47,47,34,47,47,47,34,47,34,47,34,34,47,47,47,47,34,47,34,47,34,47,34,34,34,47,34,34,34,47,34,34,47,34,47,34,47,47,34,34,47,34,47,47,47,34,47,34,47,34,47,47,47,47,34,34,34,34,34,34,34,47,47,47,47,34,47,34,34,47,34,47,34,34,34,47,47,34,34,34,47,34,47,47,47,34,34,47,47,47,47,34,34,34,47,47,34,47,34,34,34,34,34,47,47,47,47,47,34,34,34,34,47,47,34,47,47,47,34,34,47,34,34,34,34,34,34,34,47,47,34,47,34,47,47,34,47,47,47,34,34,47,47,34,34,34,47,47,47,34,34,34,34,47,34,47,34,34,47,47,47,47,34,47,34,47,47,47,47,34,34,47,47,47,34,47,34,47,34,34,47,34,47,47,47,34,34,34,34,47,47,47,34,34,47,47,47,34,34,47,34,47,34,47,34,47,34,34,47,47,47,34,47,34,47,47,47,34,34,34,34,34,47,34,47,47,47,47,34,47,47,47,47,34,34,47,47,47,34,34,34,34,34,47,34,47,47,34,47,47,47,34,47,34,47,47,34,47,34,47,34,34,47,34,34,47,34,34,34,34,34,47,34,47,34,47,47,34,47,47,34,34,47,34,34,47,34,34,47,47,34,47,34,34,47,47,47,47,47,34,47,47,47,47,34,34,34,47,47,34,34,34,47,34,34,47,47,34,34,47,34,34,34,47,47,47,34,34,34,47,47,47,34,47,47,34,47,34,34,47,47,47,34,47,34,47,34,34,47,34,34,47,47,34,34,47,47,34,34,47,47,47,34,34,47,34,34,47,47,47,34,34,47,34,34,34,47,47,47,34,34,47,47,34,34,47,47,34,34,47,47,47,47,47,34,47,47,47,34,47,47,34,34,47,34,47,34,34,34,47,47,47,47,47,47,34,34,47,47,47,34,34,34,34,34,34,34,34,47,34,34,34,34,34,47,34,34,34,47,47,34,34,34,47,34,47,47,34,47,34,34,34,47,47,34,47,34,47,34,34,47,34,47,34,34,47,47,34,34,34,47,34,34,34,34,47,34,47,47,34,34,34,47,47,34,34,34,47,47,47,34,34,47,34,47,34,47,34,34,34,47,34,47,34,34,34,47,47,34,34,47,34,47,34,34,34,34,47,47,47,47,47,34,47,47,34,47,34,34,34,34,34,34,34,47,47,34,34,47,47,47,34,34,34,47,34,34,34,34,34,47,34,47,47,34,47,47,34,34,34,34,47,34,34,47,47,34,34,34,34,47,47,47,47,34,47,34,47,47,34,34,47,34,47,47,34,34,34,34,34,34,34,47,34,34,34,47,34,34,34,34,34,47,47,47,47,34,47,47,34,34,47,34,47,47,34,34,34,47,47,34,47,47,47,47,47,34,47,34,34,47,47,34,34,34,47,47,34,34,47,34,34,34,47,34,34,47,47,34,47,34,34,47,47,47,47,34,34,34,34,34,34,34,47,47,47,34,34,47,47,47,34,47,34,47,34,34,47,47,47,47,34,47,34,47,47,34,34,34,34,47,47,47,47,34,34,47,34,34,47,34,34,47,34,47,34,34,47,34,34,34,47,34,34,34,47,47,47,34,47,34,34,47,47,47,34,34,47,34,47,47,34,47,47,47,47,47,34,34,34,47,34,34,34,34,47,34,34,47,34,34,34,34,47,47,34,47,47,34,47,34,34,47,34,47,47,47,34,47,34,34,34,47,47,47,47,34,47,47,34,34,47,47,34,47,47,34,47,34,34,47,34,34,34,34,34,34,47,47,47,34,47,34,34,34,47,47,34,47,34,47,34,47,34,34,47,34,34,34,47,34,34,47,34,34,47,47,47,34,47,47,34,34,47,47,34,34,34,34,34,34,47,47,34,34,47,34,34,47,34,47,47,34,47,47,34,47,34,34,34,47,34,34,47,34,34,34,34,47,47,34,47,34,34,34,47,47,47,34,34,34,47,34,47,34,34,34,34,47,34,34,34,34,34,47,34,34,34,47,47,34,34,34,47,34,34,47,34,34,34,34,47,34,47,34,34,47,34,34,47,47,47,47,47,34,47,34,47,47,47,47,47,47,47,47,47,34,34,34,34,47,47,47,34,47,47,34,47,47,47,47,34,47,34,34,34,47,34,34,47,47,34,47,47,34,34,34,47,34,34,47,47,47,47,47,34,47,34,34,34,47,47,47,47,47,47,34,47,47,47,47,34,47,34,34,34,34,34,34,47,47,34,34,34,34,47,34,47,47,47,34,34,47,47,47,34,47,34,47,47,34,47,47,34,47,47,34,34,47,47,47,47,34,47,47,47,34,47,47,34,34,34,34,34,34,47,34,47,47,47,47,34,34,34,34,47,47,34,47,34,47,47,34,47,34,34,34,47,34,34,47,47,47,47,47,34,34,34,47,34,47,47,34,34,47,34,34,34,47,34,47,34,47,34,47,47,47,34,34,34,34,34,34,47,47,47,47,34,34,47,47,34,34,47,47,47,34,34,34,47,34,34,34,34,34,47,34,34,34,34,34,34,47,34,47,34,34,47,47,47,47,34,34,34,34,47,47,34,47,34,47,34,34,47,34,47,47,47,34,34,34,34,47,34,47,34,47,47,47,34,34,47,47,47,47,34,34,34,47,34,47,47,34,47,34,47,34,47,47,47,47,34,34,47,47,47,47,47,47,47,34,47,34,34,47,47,47,34,47,34,34,47,34,47,47,34,47,47,34,34,34,34,34,47,34,34,34,34,47,34,47,34,34,47,47,47,47,47,34,34,34,47,34,34,47,47,47,47,34,34,34,47,34,34,47,34,47,34,34,47,47,47,34,34,34,47,34,47,47,47,47,34,47,34,47,34,47,34,47,34,34,47,34,47,34,47,47,47,34,34,47,47,34,34,34,47,47,34,34,34,34,34,34,47,34,34,34,47,34,34,34,47,47,34,34,47,47,34,47,47,34,47,34,47,47,47,47,34,34,47,34,34,47,34,34,47,47,34,47,34,34,34,34,34,34,34,47,34,34,47,47,34,47,34,34,34,47,34,34,34,47,47,47,47,47,47,47,47,47,47,34,47,47,47,34,47,34,34,47,34,47,34,47,47,47,34,34,47,34,34,34,47,34,47,34,34,34,47,34,34,47,34,34,34,34,47,47,34,47,34,47,34,47,47,47,34,34,47,34,34,34,47,47,34,34,34,47,47,47,47,34,34,47,47,47,47,34,34,47,47,47,34,34,47,34,47,34,34,34,47,34,34,34,47,34,47,47,34,47,34,34,34,34,47,34,47,34,47,47,47,47,47,34,34,34,47,47,34,34,34,47,47,34,34,34,47,47,47,47,47,34,34,47,47,34,34,47,34,47,47,47,47,47,34,34,47,47,34,34,47,34,34,47,34,34,47,47,47,47,34,34,47,34,34,34,34,34,47,34,47,47,47,47,47,47,34,34,47,34,34,34,47,47,34,47,34,34,34,34,47,34,47,47,34,34,34,34,34,34,47,47,47,47,34,34,47,34,47,34,47,47,34,34,34,34,34,47,34,47,34,34,47,34,47,47,47,34,34,34,34,47,34,47,34,47,47,34,34,47,34,34,34,34,34,47,47,34,47,47,34,47,47,34,34,47,47,47,47,34,47,47,34,34,34,34,34,34,47,34,47,34,47,34,47,34,47,34,47,34,34,47,47,47,47,34,47,34,47,34,34,34,34,47,47,34,34,47,34,34,47,47,34,34,47,47,34,34,34,34,47,47,47,34,47,47,34,47,34,47,47,47,34,47,47,34,47,34,34,34,34,34,34,34,34,47,47,34,34,34,34,47,34,47,47,47,47,47,34,47,47,47,34,47,47,47,47,47,34,47,34,34,47,47,34,47,34,34,34,47,47,34,34,47,47,47,47,34,47,34,47,47,34,34,34,47,47,47,47,34,34,34,47,47,34,34,34,47,34,47,47,47,34,47,34,34,47,34,47,47,34,34,34,34,47,47,47,34,34,34,34,47,47,34,47,47,47,34,34,34,47,47,34,47,34,47,34,47,34,47,47,47,34,34,34,34,34,47,34,47,47,47,47,34,47,34,34,47,34,34,34,47,34,47,34,34,47,47,47,47,34,34,47,34,47,34,34,34,34,34,34,34,47,47,47,34,47,47,34,47,47,34,34,34,34,47,34,47,47,34,34,47,34,47,34,34,34,47,34,47,34,34,34,47,34,34,47,34,47,34,47,34,47,47,34,34,34,34,47,47,34,34,34,34,34,34,34,47,47,34,34,47,47,47,47,34,34,47,34,34,47,34,47,34,34,47,47,47,34,34,47,34,34,34,47,47,47,34,34,47,34,34,34,47,34,34,34,47,34,34,47,34,34,47,34,47,34,34,34,34,47,34,34,34,34,47,34,47,47,47,34,34,34,34,34,47,47,47,47,34,34,47,47,34,47,47,34,34,34,47,34,47,34,47,47,34,34,34,47,47,47,34,47,34,47,34,47,47,47,34,34,47,34,34,47,34,34,47,34,47,34,47,34,34,47,34,34,34,47,34,34,34,47,34,34,47,34,47,34,47,34,34,34,34,47,34,34,47,47,47,47,47,47,34,47,47,34,47,34,34,34,47,34,34,47,47,47,34,34,34,47,34,47,47,47,47,47,47,47,34,34,47,34,47,34,34,47,34,34,47,47,34,34,47,47,47,34,34,34,47,47,34,47,47,34,34,34,47,34,47,47,47,47,47,47,47,47,34,47,34,34,47,47,34,34,34,34,47,34,47,47,34,47,34,47,47,47,34,34,47,34,47,47,47,47,34,34,47,34,34,47,47,34,47,47,47,47,34,47,47,47,47,47,47,47,34,34,47,47,47,34,47,47,34,34,47,47,34,47,34,47,47,47,34,47,47,47,47,47,34,47,47,47,47,34,47,34,34,47,34,47,34,34,34,34,34,34,34,34,34,47,47,34,47,34,47,47,47,34,34,47,34,47,34,47,47,47,47,47,34,34,34,34,34,34,47,47,47,34,34,34,47,47,34,34,47,47,34,47,34,34,47,34,34,34,47,47,34,34,34,47,47,34,47,34,47,47,34,47,34,34,34,34,47,47,47,34,47,47,47,47,47,47,47,47,47,34,47,34,47,34,47,47,34,34,34,34,34,47,47,47,34,34,47,34,47,34,47,34,34,47,34,47,47,47,34,47,34,47,34,34,34,34,47,34,47,47,34,34,34,34,47,34,47,47,47,34,47,47,34,34,47,34,34,34,47,47,47,34,47,47,34,34,34,47,34,47,34,47,47,47,34,34,47,34,34,47,34,34,34,47,34,47,47,47,47,47,47,34,34,34,47,47,47,34,47,47,47,34,47,34,34,34,34,47,47,47,47,34,34,34,34,34,47,47,34,47,34,34,47,34,34,47,34,47,47,34,47,34,34,47,34,34,34,47,47,34,47,34,34,47,47,47,34,47,34,47,47,34,34,47,47,47,47,47,47,47,34,34,47,34,34,47,47,47,47,47,47,47,34,47,47,47,34,34,47,34,47,47,34,34,34,34,47,47,34,34,34,34,34,34,34,34,34,34,47,34,47,47,34,34,34,47,47,47,34,34,34,34,47,34,47,47,34,47,47,47,34,34,34,34,34,47,34,47,47,34,34,34,47,34,34,47,47,47,47,47,34,34,47,47,34,47,34,34,47,34,47,34,47,34,47,47,34,34,34,34,34,47,34,34,34,47,47,47,34,34,47,47,47,47,34,34,34,34,47,47,47,34,34,34,47,47,34,47,34,47,34,47,47,47,47,34,34,47,47,34,34,47,34,47,47,34,47,34,47,47,47,47,34,34,47,47,34,34,47,34,47,34,34,34,47,47,47,47,34,34,47,47,47,34,47,34,34,47,47,34,34,34,47,34,34,47,47,34,47,47,34,34,47,34,47,34,47,34,47,34,47,47,34,47,47,34,47,34,34,34,34,47,47,47,34,47,47,47,47,47,34,47,34,34,47,34,47,34,34,34,34,47,47,47,47,34,47,34,34,34,34,34,47,47,34,34,47,47,34,34,34,34,47,34,34,47,47,34,47,34,47,34,34,47,47,47,47,34,47,34,34,34,34,34,34,34,34,47,47,34,47,34,47,47,47,34,47,34,47,47,34,34,34,47,34,47,34,34,34,34,47,47,34,34,34,47,34,34,34,34,34,47,34,47,47,47,47,34,34,47,47,34,34,47,47,34,47,47,47,34,34,47,34,47,34,47,34,34,47,47,47,47,34,34,34,47,34,47,34,34,47,47,47,34,47,47,47,47,47,47,34,47,47,47,47,47,34,47,34,47,34,34,34,34,47,34,47,34,34,47,34,34,34,34,47,47,47,47,47,47,47,47,34,47,34,34,47,34,47,34,47,47,47,34,47,34,47,34,34,47,47,47,47,47,47,34,34,34,47,47,47,47,34,34,47,34,34,34,34,47,34,34,34,34,34,47,47,47,47,47,47,47,47,47,47,34,47,47,34,47,47,47,34,34,34,47,47,47,47,47,34,47,47,47,47,34,34,34,47,34,34,47,47,34,47,34,34,47,47,47,34,47,47,47,34,34,34,34,34,47,47,47,47,34,47,34,47,47,34,34,34,34,34,47,34,47,34,47,34,34,47,47,47,47,47,34,34,47,47,47,34,47,34,34,47,47,47,47,34,34,34,34,34,34,47,47,34,34,34,34,34,34,47,47,34,47,47,34,34,47,34,47,34,47,34,47,47,34,34,47,47,34,47,34,47,34,47,34,34,34,34,34,34,47,47,34,34,34,47,47,34,34,34,34,47,34,34,34,47,47,34,47,34,34,34,47,47,47,34,47,34,34,47,34,34,47,47,47,47,47,34,34,34,34,47,34,47,34,47,34,34,47,34,47,34,47,34,34,47,47,47,47,34,47,47,47,47,47,47,47,34,47,47,34,47,47,47,34,47,47,47,34,34,47,47,34,47,34,47,47,34,47,47,47,47,34,47,47,47,34,34,47,47,47,34,34,34,34,47,34,47,34,47,34,47,47,34,47,47,34,34,34,47,34,34,34,47,34,34,34,47,34,47,47,34,34,34,47,34,47,47,34,34,47,34,34,47,47,34,34,34,34,47,34,47,34,47,47,34,47,34,34,47,47,47,34,47,47,34,34,47,47,47,34,34,47,34,47,47,47,47,47,34,47,47,34,47,47,47,47,47,47,47,34,34,47,47,47,47,34,34,47,47,47,47,34,47,47,34,34,34,47,34,34,34,34,34,47,34,47,34,34,47,34,47,47,34,34,34,47,34,47,34,47,34,47,34,47,34,47,47,47,34,47,47,34,34,34,34,47,34,34,47,47,34,47,34,34,47,47,34,47,47,34,34,47,34,34,34,47,34,47,47,47,34,47,34,47,47,34,47,34,47,34,47,47,47,34,47,47,47,47,47,34,34,47,47,34,34,34,47,47,47,34,47,34,47,34,47,47,47,34,47,34,47,34,47,34,34,47,47,34,34,47,47,47,34,34,34,47,34,47,34,34,34,47,34,34,47,34,47,47,34,34,34,34,47,47,47,47,47,47,34,47,34,34,47,47,47,34,47,47,47,34,34,34,34,34,47,47,47,47,34,34,47,47,47,47,47,34,34,47,34,47,47,47,34,34,34,34,47,47,34,47,34,47,34,34,34,47,34,47,47,47,34,34,34,47,47,34,34,34,34,47,47,47,47,47,34,34,47,47,34,34,34,34,47,47,47,34,34,34,34,34,34,34,34,47,34,47,34,34,34,47,47,34,34,47,34,47,47,34,34,47,47,47,34,47,34,47,34,34,34,47,47,47,47,47,34,34,34,47,47,47,34,34,34,47,34,34,47,34,34,47,47,34,34,34,34,34,47,47,47,34,47,47,47,34,34,47,34,47,34,34,34,47,34,47,47,34,47,47,47,47,47,47,47,47,47,47,34,34,47,47,47,47,34,47,47,34,47,34,34,47,47,34,47,47,34,47,34,34,34,34,47,47,34,47,34,47,34,47,47,34,47,34,47,34,47,34,47,47,34,47,47,47,47,47,47,34,47,47,34,34,34,34,47,34,47,47,47,34,34,47,34,47,34,34,47,34,34,34,34,34,34,34,47,47,47,47,47,34,34,47,47,47,47,34,34,47,34,34,34,47,47,34,47,47,34,34,47,47,34,47,34,47,34,47,47,47,47,34,34,34,47,34,47,34,34,47,47,34,47,34,34,34,34,47,47,47,34,47,47,47,47,47,47,47,34,34,34,34,34,34,34,34,47,34,34,47,34,47,34,47,34,34,47,47,47,34,47,47,34,47,47,34,47,34,34,47,34,47,34,34,47,34,34,34,34,34,47,47,47,47,47,47,47,34,34,47,47,47,34,47,47,34,47,34,34,34,47,34,34,47,34,47,47,34,47,47,47,47,47,34,34,47,34,34,34,34,47,47,47,47,34,34,34,34,34,34,47,34,34,34,47,34,47,47,34,34,34,47,34,34,34,47,34,47,34,47,34,47,47,34,47,47,34,47,47,47,47,34,34,47,47,47,34,34,47,34,34,34,47,34,34,34,47,47,34,47,47,34,34,34,34,47,47,47,47,47,47,34,34,34,47,34,34,34,34,34,47,34,34,47,34,34,34,47,47,34,47,47,47,47,34,34,47,34,34,47,47,34,47,34,34,47,34,47,34,47,34,47,34,34,34,34,34,34,47,34,34,47,47,34,34,34,47,34,34,34,34,47,34,34,47,47,47,47,34,34,34,47,34,47,34,34,47,47,34,47,47,34,47,47,34,34,34,34,47,47,47,34,34,47,47,47,34,34,47,47,34,47,34,34,34,47,47,47,34,34,34,34,34,34,47,34,47,34,34,34,34,47,47,47,34,47,47,34,47,34,47,47,34,34,47,47,47,34,47,47,34,34,34,34,34,47,34,47,34,47,47,34,34,47,47,34,47,47,34,47,47,34,47,47,47,34,47,34,47,34,34,47,47,47,34,47,34,47,47,47,47,47,47,47,34,34,34,47,47,47,34,47,47,34,47,34,47,47,47,34,47,47,34,47,47,47,47,47,34,34,47,47,34,47,47,34,47,34,34,47,34,34,34,34,34,47,34,34,47,34,34,47,34,47,47,47,34,34,34,47,34,47,34,34,47,47,34,34,34,34,34,34,34,34,47,34,47,47,34,47,34,47,34,34,34,47,34,47,34,47,47,34,47,47,47,47,47,34,34,34,47,34,34,34,47,34,47,47,34,34,34,34,34,34,34,47,47,47,34,34,47,34,34,47,47,47,47,34,47,34,47,34,47,34,47,47,47,47,47,47,47,47,47,47,47,34,47,34,34,34,47,34,34,47,47,47,34,34,47,34,34,34,34,34,47,34,47,47,34,34,34,47,47,47,47,47,47,34,47,34,34,47,47,34,47,47,34,47,34,34,34,34,34,47,34,34,47,34,34,34,34,47,34,34,34,34,47,34,47,34,34,47,47,47,47,47,34,47,34,47,34,34,34,47,34,47,47,47,34,47,34,34,47,34,34,47,47,47,34,34,34,47,34,47,47,47,34,47,47,34,34,34,34,34,34,34,34,34,47,34,47,34,34,34,34,47,47,34,47,34,34,34,47,47,47,47,47,34,34,34,47,34,47,47,47,47,34,47,34,34,34,34,47,47,34,47,34,47,47,47,34,34,34,34,34,47,47,47,47,34,34,34,47,47,47,34,47,47,47,34,47,34,34,47,47,47,34,47,34,34,34,47,34,34,47,47,47,34,34,47,34,34,34,47,47,34,34,34,47,34,47,34,34,47,34,34,34,47,47,47,34,34,34,47,47,34,47,47,34,47,34,47,47,47,34,47,47,34,34,34,47,34,34,34,34,34,34,47,47,34,34,47,34,34,34,34,34,47,34,47,34,47,34,34,47,34,47,47,34,47,34,34,47,34,34,47,47,47,34,47,34,47,47,47,47,34,34,47,47,34,34,34,34,34,47,34,47,34,34,34,47,47,34,34,47,47,34,47,34,47,34,34,47,34,34,47,34,47,34,47,34,47,47,47,34,34,34,34,34,34,47,47,34,34,34,34,34,34,34,34,34,47,34,47,47,34,47,34,47,34,34,47,47,47,34,34,47,34,47,47,34,47,34,34,34,47,34,34,34,47,47,34,34,47,34,34,34,47,34,47,34,34,34,47,47,34,34,47,34,34,34,47,47,34,34,47,34,34,47,34,47,34,47,47,34,47,47,34,34,34,47,34,47,47,47,47,47,47,34,47,34,47,34,34,34,47,47,34,34,47,34,34,47,34,34,47,34,34,34,34,47,34,34,34,34,34,47,47,47,34,47,47,47,34,34,34,34,47,34,34,47,47,34,34,34,47,34,47,47,34,47,47,34,47,34,34,34,47,34,47,47,34,47,34,34,47,47,34,34,47,34,47,47,47,47,34,47,47,34,34,47,47,47,47,47,47,47,47,47,47,47,34,47,34,47,47,47,47,47,34,47,47,34,34,34,34,34,47,34,47,47,34,34,47,34,47,34,34,47,47,34,47,47,47,47,34,47,34,47,34,34,47,47,34,34,34,34,47,47,47,47,34,34,34,47,34,34,47,47,34,47,34,47,34,47,47,34,47,47,47,34,47,34,47,34,34,47,47,47,34,47,47,47,47,47,34,47,47,47,34,34,47,47,47,47,34,34,47,34,34,47,47,34,34,47,34,47,47,34,34,47,34,47,47,47,34,34,47,47,47,34,34,47,34,34,34,47,47,47,47,47,47,34,34,47,34,34,34,34,47,34,34,47,34,47,47,34,47,34,47,47,34,47,47,34,34,47,34,47,34,47,34,47,47,34,47,47,34,47,34,47,34,47,34,34,34,47,47,47,34,34,47,34,34,47,47,47,47,47,47,47,34,34,47,34,34,34,47,34,34,34,47,34,47,34,34,34,47,34,47,47,47,47,34,47,47,34,47,47,47,34,47,34,34,34,47,34,34,34,34,34,47,34,47,47,34,47,47,47,47,34,47,47,47,47,34,47,47,47,47,34,47,47,47,47,47,34,34,34,47,34,34,47,34,47,47,34,47,47,34,34,47,34,34,47,34,47,47,34,34,34,47,47,47,47,34,34,34,47,34,47,47,34,34,47,34,34,47,34,47,47,34,47,47,34,34,34,47,47,47,34,34,47,34,47,47,34,34,47,47,34,47,47,47,47,47,47,47,34,47,47,47,34,34,34,34,47,47,34,47,34,34,47,34,34,34,47,34,34,34,47,34,34,34,47,34,34,34,47,47,34,47,47,34,47,34,47,47,34,34,34,47,34,47,34,47,47,47,34,47,47,47,47,47,34,47,34,47,47,34,34,34,47,34,34,47,47,34,34,34,34,47,47,47,47,47,34,34,47,47,34,47,34,34,34,47,34,34,34,47,34,34,34,34,34,47,47,47,34,47,34,34,34,47,34,34,47,34,47,34,47,34,47,47,34,34,47,34,47,34,34,47,47,34,47,47,34,34,47,47,34,34,34,47,34,34,47,34,47,34,34,47,47,34,34,47,47,47,34,47,47,47,47,47,34,47,34,34,47,34,34,47,47,34,47,34,34,47,34,34,47,47,34,47,34,47,34,47,47,47,47,34,34,47,47,34,47,34,47,34,34,47,34,47,47,47,47,34,34,47,47,47,47,34,47,47,47,47,34,34,47,34,47,47,47,34,34,34,34,34,34,47,47,47,34,34,47,47,47,34,34,34,34,47,34,47,34,47,34,34,34,34,47,47,47,34,47,34,47,34,34,47,47,34,34,47,47,47,34,34,34,34,47,47,47,34,34,47,47,47,47,47,47,34,34,47,47,47,47,34,34,47,34,34,34,34,34,34,47,47,47,47,34,47,34,47,34,34,47,47,47,34,34,47,47,47,34,47,34,47,34,34,47,34,34,34,34,34,34,34,34,34,34,34,47,47,47,34,34,34,47,47,34,34,34,47,47,47,34,47,34,34,34,34,34,34,34,47,34,34,47,47,47,47,34,47,34,34,47,34,34,47,34,34,47,47,47,47,47,47,47,34,34,34,34,47,34,34,34,34,47,34,47,47,34,47,34,34,47,34,47,34,47,47,47,34,34,47,47,47,47,47,47,34,47,34,34,47,34,34,47,47,47,47,47,47,34,47,34,34,34,34,47,47,34,34,47,34,34,47,47,47,34,34,47,34,34,34,34,34,47,34,47,34,47,34,34,34,47,34,34,34,34,47,47,47,47,47,34,34,47,34,34,47,34,34,34,34,47,34,34,47,47,47,47,47,34,34,47,47,34,47,34,34,34,34,47,34,34,47,47,47,47,47,34,34,34,47,34,34,34,34,34,47,47,47,34,47,34,47,34,47,47,47,34,47,47,47,47,47,34,34,34,47,34,47,34,47,47,47,34,47,34,34,47,34,34,34,47,47,47,47,34,34,47,34,47,34,47,34,34,34,34,34,34,47,47,34,34,47,34,34,47,34,34,47,34,34,47,47,47,34,34,34,47,47,47,47,34,47,47,47,34,47,34,47,47,47,34,47,34,34,47,34,47,47,47,47,34,47,47,34,47,34,47,47,47,34,47,47,47,47,47,34,47,47,34,34,47,34,47,34,34,34,47,47,34,47,34,47,34,34,34,47,47,47,34,47,34,34,47,34,34,34,47,47,47,47,47,47,47,34,47,34,34,47,34,34,47,47,34,47,34,34,34,34,47,34,47,34,47,47,47,47,47,34,47,47,47,34,34,47,47,34,34,47,47,47,34,47,47,34,34,34,47,47,47,34,34,34,47,34,47,47,34,47,47,47,34,47,47,34,47,47,34,47,47,34,34,34,47,47,47,34,47,34,34,47,34,47,34,47,47,34,47,47,47,47,47,34,47,34,47,47,34,34,34,47,47,34,34,47,47,47,47,47,34,34,34,47,47,34,47,47,47,34,34,34,34,47,47,34,34,47,47,47,47,47,34,34,34,47,47,34,47,47,47,34,34,47,34,34,47,34,47,34,47,34,34,47,34,47,47,34,34,47,34,34,34,34,47,34,34,47,47,47,47,47,47,47,34,34,34,34,34,34,34,34,47,47,34,34,47,47,47,47,34,47,47,47,34,34,47,47,34,34,34,34,47,34,34,47,47,34,34,47,47,34,34,34,34,34,34,47,47,34,47,47,34,34,47,34,34,34,34,47,34,34,34,34,34,34,47,47,47,47,34,47,34,34,34,34,47,47,34,34,47,47,47,47,47,34,34,47,47,47,47,47,47,47,47,47,34,34,47,34,47,47,34,47,47,47,34,34,47,47,34,34,47,47,47,34,34,47,34,34,34,34,34,34,47,47,47,47,34,47,47,34,34,47,34,47,34,34,34,47,34,34,47,34,34,34,34,34,47,34,34,47,47,34,34,34,47,47,34,47,47,47,47,47,34,47,34,47,34,34,34,34,47,34,47,34,34,47,47,34,34,47,34,34,34,34,47,47,34,47,34,34,34,34,47,47,47,47,47,47,34,34,47,47,34,34,34,34,34,34,47,34,47,47,34,47,34,47,34,34,34,47,34,34,34,34,34,34,47,47,34,34,47,34,34,47,47,34,34,47,34,34,47,47,34,34,34,34,34,47,34,47,47,47,47,47,34,47,47,34,47,47,34,47,47,34,34,47,34,47,47,47,47,34,47,34,47,34,47,34,47,47,34,47,47,47,47,47,34,34,34,47,47,34,47,47,47,47,34,34,47,47,34,47,34,47,34,34,34,47,34,47,47,34,47,47,34,34,34,47,47,34,34,34,47,47,34,47,47,34,34,34,34,34,47,34,47,34,47,47,34,34,47,34,47,34,34,34,34,47,47,34,47,34,47,34,34,47,34,47,34,34,34,47,47,47,47,34,34,47,47,47,47,34,34,47,47,34,34,47,34,34,47,34,47,47,34,47,34,34,47,47,47,34,47,47,47,47,34,47,34,34,34,34,34,34,34,34,47,34,34,34,34,47,47,47,47,34,47,34,34,34,47,34,34,34,47,34,47,34,34,34,34,47,34,34,34,47,34,47,47,47,34,34,47,47,47,47,47,34,47,47,47,47,34,34,47,34,34,47,34,47,34,47,34,34,47,47,47,34,47,47,34,34,34,47,34,34,47,47,47,34,47,34,34,47,47,47,47,34,34,47,34,47,34,47,34,47,34,34,47,47,47,34,34,34,34,47,34,47,47,47,47,47,34,47,47,47,34,34,47,47,34,47,34,34,34,34,47,34,34,47,34,47,34,47,47,34,34,47,47,34,34,47,34,47,47,34,47,47,34,34,34,34,47,34,47,47,47,34,47,34,34,34,34,34,47,47,34,47,47,47,34,34,47,34,47,34,34,47,34,34,47,47,47,34,47,34,34,34,47,34,34,34,47,47,47,34,34,34,47,47,47,34,34,34,34,34,34,47,34,47,34,34,47,34,34,47,34,47,47,34,47,47,34,47,34,34,47,34,34,34,47,34,47,47,47,34,47,34,47,47,34,47,34,34,47,47,34,34,47,47,47,34,47,47,47,34,34,47,47,34,34,47,34,47,34,34,34,34,47,47,34,47,47,47,47,34,34,47,34,34,34,47,47,34,34,34,47,34,47,34,34,34,47,47,47,47,34,34,47,47,34,47,47,47,47,34,34,47,47,47,34,47,47,47,47,47,47,34,34,47,47,34,34,34,34,47,47,47,34,34,47,47,47,47,47,34,47,34,47,47,34,34,34,47,34,34,34,34,47,47,34,47,47,34,34,47,34,34,47,34,34,34,47,47,34,34,47,34,34,47,47,47,34,34,47,34,47,34,34,34,47,34,47,47,34,34,34,34,34,47,34,47,47,47,47,47,34,34,34,34,47,34,47,34,47,47,34,34,34,47,47,47,47,47,47,34,47,47,47,47,47,34,47,34,34,34,34,47,34,34,34,34,47,47,34,47,34,47,34,47,47,34,34,34,47,34,47,47,47,34,47,34,47,47,34,47,34,47,47,34,47,47,47,47,34,47,34,47,47,47,34,34,47,47,34,47,34,34,34,34,47,34,47,34,47,34,34,34,34,34,47,34,47,47,34,34,34,47,34,34,34,47,47,47,47,34,34,47,34,34,47,47,47,34,47,34,34,47,47,47,34,34,34,34,34,34,47,34,34,34,47,47,47,34,34,34,34,47,47,47,34,34,47,47,47,47,47,34,47,34,34,34,47,34,34,47,47,34,34,47,34,34,47,47,47,34,47,34,47,34,47,47,47,34,47,47,47,34,47,34,47,47,34,47,34,34,47,34,47,34,34,47,47,47,34,47,34,34,47,47,47,47,47,34,47,47,47,34,34,34,34,47,34,47,34,34,34,34,34,34,34,47,47,47,47,34,47,47,47,47,47,34,34,34,47,47,47,47,47,34,34,47,47,34,34,47,47,34,34,47,34,34,34,34,34,47,47,34,34,47,34,34,34,47,47,47,47,47,34,34,34,47,34,34,47,34,47,47,47,47,47,47,34,34,47,47,47,34,34,47,47,47,34,47,34,34,34,47,47,47,47,47,47,47,34,47,34,34,34,34,47,47,34,47,47,34,47,47,34,34,47,47,34,47,47,47,34,34,34,34,34,34,34,34,34,34,47,34,47,34,47,34,34,34,34,47,34,34,34,34,34,34,47,34,47,34,34,34,47,47,34,47,47,34,34,47,34,47,34,47,34,34,47,47,47,34,47,34,47,34,47,47,34,47,34,47,47,34,34,34,34,47,34,47,34,34,34,34,34,34,34,47,47,34,47,34,47,47,34,47,34,34,34,47,47,34,34,47,34,47,47,34,47,34,47,47,34,34,47,47,34,34,34,47,34,34,34,47,47,34,34,47,47,34,47,34,47,34,47,47,34,34,47,34,47,34,47,47,34,47,47,34,47,47,34,34,47,34,34,34,34,47,47,47,34,34,34,47,34,47,47,34,34,34,34,47,34,34,47,47,47,47,47,34,34,34,47,34,47,34,47,34,34,34,34,47,47,47,47,47,34,47,47,34,34,34,47,34,47,34,47,34,47,34,47,34,34,34,47,47,47,34,34,34,47,34,34,34,47,47,47,34,47,34,47,34,34,47,34,47,34,34,34,34,34,47,47,47,47,34,34,34,34,47,34,47,47,34,47,34,34,47,47,47,34,34,47,47,34,47,34,34,34,34,34,34,34,47,47,34,34,47,34,34,34,47,47,47,34,34,34,47,47,34,34,47,34,47,47,34,47,47,47,47,34,34,47,47,47,47,34,34,47,34,47,47,47,47,34,34,34,47,47,34,34,47,34,47,34,47,34,47,47,47,34,47,47,34,47,34,34,34,34,47,34,34,47,34,34,47,47,34,47,34,34,47,47,47,47,34,47,47,34,34,34,34,47,34,34,34,34,47,47,34,34,47,47,34,34,34,47,47,34,34,47,34,47,47,47,47,47,34,34,47,34,47,34,47,47,47,47,47,47,47,34,47,34,47,47,47,47,47,47,47,47,34,34,34,47,47,34,47,34,47,34,34,47,47,47,47,47,34,47,34,47,34,34,47,47,47,47,34,34,34,34,47,34,34,34,34,47,34,47,34,34,47,34,34,47,47,34,34,47,47,47,47,47,34,34,47,34,34,34,34,47,47,34,47,47,47,47,47,47,34,47,47,47,47,47,47,47,47,47,47,34,47,47,34,34,47,47,47,34,47,34,34,34,34,34,34,47,47,47,34,34,34,47,34,34,34,34,47,47,34,34,47,47,47,47,34,47,34,47,47,47,47,47,34,34,34,47,34,34,47,47,34,47,34,34,47,34,47,47,47,34,34,47,34,34,47,34,34,47,47,47,47,47,47,47,47,47,34,47,34,34,34,47,47,34,34,47,34,47,34,34,34,47,47,47,34,47,47,34,34,47,47,34,34,34,47,47,47,47,34,47,47,47,34,34,47,47,34,34,47,47,47,47,47,47,34,34,34,47,34,34,34,47,34,47,47,34,34,47,47,34,47,34,47,47,47,34,34,47,47,34,34,34,34,47,47,47,47,34,34,34,34,34,47,34,34,47,34,47,34,34,34,47,47,47,34,47,34,34,34,47,34,34,47,47,47,47,47,47,34,47,47,34,47,47,34,47,47,34,47,47,47,34,34,47,47,34,34,34,34,34,34,47,34,34,47,34,34,34,34,47,47,47,34,34,47,34,34,34,34,47,34,34,34,47,34,47,47,34,47,34,34,34,47,34,34,34,47,34,47,34,34,47,34,47,47,34,47,47,34,34,34,34,34,34,47,47,47,47,47,34,47,34,34,47,47,34,47,47,34,47,47,47,34,34,47,47,47,34,34,47,34,47,47,47,34,34,34,47,47,47,47,47,47,34,47,47,47,47,47,34,34,34,47,34,34,47,47,47,47,34,47,34,34,34,47,47,34,34,47,47,47,47,47,47,34,47,34,47,47,34,34,47,34,34,34,47,34,47,47,47,34,47,47,34,47,34,34,47,34,34,47,47,47,47,47,34,34,34,47,34,34,34,47,34,47,47,47,47,47,34,47,34,47,47,47,47,34,47,34,47,47,47,47,47,47,47,34,34,34,34,34,47,34,34,47,34,47,34,34,47,47,47,47,47,47,47,34,47,47,47,47,34,34,47,47,34,34,34,47,47,34,34,34,47,34,47,34,34,34,34,47,34,47,47,34,47,47,47,47,47,47,47,47,47,34,47,47,34,47,47,47,47,47,34,47,34,34,34,47,34,34,47,47,47,34,47,34,34,34,47,47,34,34,34,47,47,34,34,47,34,34,47,34,34,34,47,34,34,34,34,34,47,47,47,34,47,47,34,47,47,34,34,47,34,34,34,47,34,34,47,34,34,47,34,34,34,34,34,34,34,34,47,47,47,47,34,34,34,34,47,34,47,47,47,47,47,34,34,34,34,47,47,47,34,47,34,34,47,47,47,47,34,47,34,47,47,47,34,34,34,47,34,47,47,34,34,34,34,34,47,47,34,34,47,47,47,47,34,47,47,34,47,47,34,47,34,34,34,47,34,34,47,34,34,47,34,47,47,34,47,34,47,34,34,34,34,47,34,47,34,34,34,47,47,47,47,47,47,47,34,34,47,34,34,34,47,47,47,34,47,34,34,47,34,47,47,47,47,34,47,47,47,34,34,47,47,47,34,34,47,34,47,34,34,47,34,34,47,34,34,34,47,47,47,34,34,34,47,34,47,34,47,34,34,47,34,34,47,34,47,47,47,34,34,34,47,47,34,47,34,47,34,47,34,34,34,47,47,47,47,34,47,47,34,47,34,34,34,34,34,34,34,34,47,47,34,34,34,34,34,47,34,34,47,47,34,47,34,34,47,47,34,47,34,34,34,34,34,34,47,47,34,34,34,47,47,47,47,47,47,47,34,34,34,47,34,34,47,47,47,47,34,47,47,34,34,47,47,34,47,47,34,34,47,47,47,47,47,34,34,34,34,47,34,47,34,34,47,34,47,47,47,34,34,47,47,47,47,34,47,34,34,47,34,34,47,34,47,47,34,47,34,47,47,47,47,47,47,47,34,34,34,34,34,34,34,34,34,47,34,47,47,47,47,47,47,47,47,34,47,47,47,47,47,47,34,47,47,47,47,34,34,34,47,47,34,47,47,47,47,47,47,34,47,34,34,34,34,34,34,34,47,34,34,47,34,47,47,34,47,34,34,34,47,34,34,34,34,34,47,47,34,34,34,47,47,47,47,47,34,47,47,34,47,34,47,47,47,34,47,34,34,47,47,47,34,47,47,47,47,47,34,47,34,34,47,34,34,47,34,34,47,34,34,47,47,34,34,47,47,47,34,47,47,47,34,47,34,34,47,47,34,34,34,47,34,34,34,34,47,34,34,47,34,34,47,34,47,47,34,47,47,34,34,47,34,34,34,47,34,47,34,34,34,34,34,47,34,34,47,34,34,34,47,34,47,34,47,47,34,34,34,34,34,47,34,47,34,34,47,47,47,34,47,34,34,47,47,47,34,34,34,34,34,34,47,47,34,47,47,47,34,34,34,34,34,34,47,47,47,47,34,34,47,47,47,47,34,34,34,34,34,47,34,47,34,34,47,47,47,47,47,34,34,34,34,47,34,34,34,34,34,34,47,34,47,34,34,47,47,34,34,47,34,47,34,34,34,47,47,34,34,47,47,47,47,34,34,34,47,34,47,47,34,47,34,34,47,34,47,47,34,47,34,34,47,47,47,47,34,47,47,47,34,47,34,34,47,34,34,47,34,47,47,47,34,34,47,34,47,34,34,34,34,47,47,34,34,34,47,34,47,34,47,34,34,34,47,34,34,47,34,34,34,47,34,34,34,47,34,47,47,47,34,47,34,34,47,47,34,47,47,47,47,47,47,47,47,34,34,47,34,34,34,34,34,47,47,47,34,34,34,47,47,34,47,34,34,34,47,47,47,47,34,34,34,34,47,47,47,34,47,34,34,47,47,47,34,47,47,34,34,47,47,34,47,47,47,34,47,47,47,34,47,34,47,47,34,34,34,47,34,47,47,47,34,47,47,47,47,34,34,34,47,34,34,47,47,34,34,34,34,34,47,34,34,47,47,34,34,47,34,34,34,34,47,47,47,47,47,47,34,34,34,34,47,34,34,34,47,47,34,34,47,47,47,47,47,47,47,34,47,47,47,47,34,34,34,34,34,34,34,34,47,34,34,34,47,47,34,34,47,34,34,34,34,47,47,47,47,47,47,34,34,47,47,34,47,47,34,47,47,34,47,34,47,34,47,47,34,47,34,34,47,34,47,34,34,34,47,47,34,34,34,47,34,47,34,34,34,47,34,47,34,47,34,47,47,34,34,47,47,47,34,47,47,47,34,34,47,34,47,47,47,47,34,47,34,47,34,34,47,34,34,47,47,47,47,47,34,47,47,47,47,47,34,47,34,47,34,34,34,47,47,47,34,47,34,34,34,47,47,47,34,47,47,34,34,34,34,34,47,47,47,47,47,47,34,47,34,47,34,34,34,34,47,47,47,47,47,34,34,47,34,47,34,34,34,34])
print(result)

""" TLE since it takes O(n^2) """
# class Solution:
#     def dailyTemperatures(self, temperatures):
#         """
#         'Given a list of daily temperatures temperatures, return a list such that, 
#         for each day in the input, tells you how many days you would have to wait
#         until a warmer temperature.
#         If there is no future day for which this is possible, put 0 instead.'

#         Args:
#             temperatures (List[int]): The list contained each day's temperature
        
#         Returns:
#             List[int]
#         """
        
#         waitday_list = []
#         for i in range(len(temperatures)):
#             day_count = 0
#             for j in range(i+1, len(temperatures)):
#                 if temperatures[i] < temperatures[j]:
#                     day_count += 1
#                     waitday_list.append(day_count)
#                     break
#                 else:
#                     day_count += 1
#                     if i + 1 + day_count == len(temperatures):
#                         waitday_list.append(0)
#                         break
#         waitday_list.append(0)
#         return waitday_list