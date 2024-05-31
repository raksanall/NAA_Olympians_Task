
# this uses stack for solving time limit exceeded
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         n = len(temperatures)
#         answer = [0] * n
#         stack = []
#         for i in range(n):
#             while stack and temperatures[i] > temperatures[stack[-1]]:
#                 index = stack.pop()
#                 answer[index] = i - index
#             stack.append(i)

#         return answer


# (this code comes to mind firstly but gives time limit exceeded)
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         n = len(temperatures)
#         answer = [0] * n
#         for i in range(len(temperatures)):
#             count=0
#             for j in range(i+1,len(temperatures)):
#                 if temperatures[j] > temperatures[i]:
#                     answer[i]=j-i
#                     break;
#         return answer