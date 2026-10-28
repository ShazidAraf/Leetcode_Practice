class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        far = 0

        for i,x in enumerate(nums):
            if i>far:
                return False

            far = max(far,i+x)

        return True








        # if len(nums)==1:
        #     return True

        # if nums[0]==0:
        #     return False

        # ways = [0]*len(nums)

        # for i in range(len(nums)-1):

        #     if i>0 and ways[i]==0:
        #         return False

        #     for j in range(i+1, min(i+nums[i], len(nums)-1) + 1):
        #         ways[j] += 1

        # if ways[-1]>0:
        #     return True
        # else:
        #     return False