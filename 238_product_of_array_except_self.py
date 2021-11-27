# https://leetcode.com/problems/product-of-array-except-self/
from functools import reduce
from typing import List


class Solution:
    # O(n) using division
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # get product and save indexes of zeros
        product = 1
        zeros = set()
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.add(i)
            else:
                product *= nums[i]

        # more then one zero case
        if len(zeros) > 1:
            return [0] * len(nums)

        # one zero case
        if zeros:
            zero = zeros.pop()
            return [0] * zero + [product] + [0] * (len(nums) - 1 - zero)

        # no zeros case
        answer = []
        for item in nums:
            answer.append(product // item)

        return answer

    # O(n) without division
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1]
        for i in range(1, len(nums)):
            product.append(product[i - 1] * nums[i - 1])

        p = 1
        for i in range(len(nums) - 1, -1, -1):
            product[i] *= p
            p *= nums[i]

        return product


if __name__ == '__main__':
    solution = Solution()
    assert solution.productExceptSelf(nums=[1, 2, 3, 4]) == [24, 12, 8, 6]
    assert solution.productExceptSelf(nums=[-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert solution.productExceptSelf(nums=[-1, 1, 0, -3, 0]) == [0, 0, 0, 0, 0]
