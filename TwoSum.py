# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1]
 
# Input: nums = [3,2,4], target = 6 Output: [1,2]

# Input: nums = [3,3], target = 6 Output: [0,1]


nums = [3,2,4]
target = 6
final_output = []

# o(n2) soln
# def two_sum(nums, target):
#     for i in range(0, len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 final_output.append(i)
#                 final_output.append(j)
#                 return final_output
#     return final_output

#o(nlogn)
# def two_sum(nums, target):
#     nums = sorted(nums)
#     left = 0
#     right = len(nums) - 1
#     while right > left:
#         if nums[left] + nums[right] > target :
#             right = right - 1
#         elif nums[left] + nums[right] < target :
#             left = left + 1
#         else:
#             final_output.append(left)
#             final_output.append(right)
#             return final_output
#     return final_output

#o(n)
def two_sum(nums, target):
    dict = {}
    for i in range(0, len(nums)):
        # 
        ele = target - nums[i]
        if ele not in dict:
            dict[nums[i]] = i
        elif ele in dict:
            final_output.append(dict[ele])
            final_output.append(i)
            return final_output
    return final_output
        
        

print(two_sum(nums, target))

