class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [ i*i for i in nums]
        return sorted(result)

        