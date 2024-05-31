# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         numbers={num for num in range (1,len(nums)+1)}
#         for i in nums:
#             if i in numbers:
#                 numbers.remove(i)
#         return list(numbers)
        