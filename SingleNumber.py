# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         dict={}

#         for num in nums:
#             if num in dict:
#                 dict[num]+=1
#             else:
#                 dict[num]=1
        
#         for num in dict:
#             if dict[num]==1:
#                 return num