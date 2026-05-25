# nums=[0,1,2,2,3,0,4,2]
# val=2
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in nums:
            if i != val:
                nums[k] = i
                k+=1
        return k
        