'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''
class Solution:
    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        # O(n^2)
        # n = len(nums)
        # output_list = [None] * len(nums)
        # for i in range(n):
        #     product = 1
        #     for j, num in enumerate(nums):
        #         if i != j:
        #             product *= num
        #     output_list[i] = product
        # return output_list

        # O(n)
        product = 1
        n = len(nums)
        output_list = []
        for i in range(n):
            output_list.append(product)
            product = product * nums[i]
        print(output_list)

        product = 1
        for i in reversed(range(n)):
            output_list[i] = output_list[i] * product
            product = product * nums[i]
        return output_list


print(Solution.productExceptSelf(0, [1,2,3,4]))
print(Solution.productExceptSelf(0, [0, 0]))
print(Solution.productExceptSelf(0, [1, 0]))

print()
class Solution:
    def productExceptSelf(self, nums: 'list[int]') -> 'list[int]':
        length = len(nums)
        L, R, answer = [0] * length, [0] * length, [0] * length
        L[0] = 1
        for i in range(1, length):
            L[i] = nums[i - 1] * L[i - 1]
        print(L)

        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            R[i] = nums[i + 1] * R[i + 1]
        print(R)

        for i in range(length):
            answer[i] = L[i] * R[i]
        return answer

print(Solution.productExceptSelf(0, [1, 2, 3, 4]))