from math import gcd, lcm

class Solution:
    def maxLength(self, nums):

        ans = 0

        for i in range(len(nums)):
            product = 1
            g = 0
            l = 1

            for j in range(i, len(nums)):

                product *= nums[j]
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])

                if product == g * l:
                    ans = max(ans, j - i + 1)

        return ans