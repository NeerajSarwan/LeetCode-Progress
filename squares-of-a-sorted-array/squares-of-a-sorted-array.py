class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = [0]*len(nums)
        
        left, right, index = 0, len(nums)-1, len(nums)-1
        
        while left<=right:
            if abs(nums[left])<abs(nums[right]):
                answer[index] = nums[right]**2
                right-=1
            else:
                answer[index] = nums[left]**2
                left+=1
            index-=1
        return answer
        