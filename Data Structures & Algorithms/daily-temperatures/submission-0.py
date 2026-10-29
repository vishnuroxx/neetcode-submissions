class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(0, len(temperatures)):
            pair = (temperatures[i], i)
            # check top of the stack 
            while stack and stack[-1][0] < pair[0]:
                prev_pair = stack.pop()
                result[prev_pair[1]] = pair[1] - prev_pair[1]
            # add this new pair to queue
            stack.append(pair)
        return result  
        

          
          
            

          