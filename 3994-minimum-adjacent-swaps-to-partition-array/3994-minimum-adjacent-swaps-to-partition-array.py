class Solution:
    def minAdjacentSwaps(self, nums: List[int], a: int, b: int) -> int:
        count_1 = 0
        count_2 = 0
        swaps = 0
        MOD = 10**9 + 7
        
        for x in nums:
            if x < a:
                # Element belongs to the first part (Group 0)
                # It must swap past all previously seen elements of Group 1 and Group 2
                swaps = (swaps + count_1 + count_2) % MOD
            elif x <= b:
                # Element belongs to the second part (Group 1)
                # It must swap past all previously seen elements of Group 2
                swaps = (swaps + count_2) % MOD
                count_1 += 1
            else:
                # Element belongs to the third part (Group 2)
                # No swaps needed relative to previously seen elements
                count_2 += 1
                
        return swaps