class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:

        odd = 0
        even = 1
        total = 0
        ans = 0

        for x in arr:
            total += x

            if total % 2:
                ans += even
                odd +=1

            else:
                ans += odd
                even +=1

        return ans % (10**9 + 7)
        