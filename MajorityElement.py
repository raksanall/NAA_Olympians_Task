# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         dict={}
#         maxCount=0
#         maxNumber=None

#         for num in nums:
#             if num in dict:
#                 dict[num]+=1
#             else:
#                 dict[num]=1
        
#         for num in dict:
#             if dict[num]>maxCount:
#                 maxCount=dict[num]
#                 maxNumber=num

#         return maxNumber