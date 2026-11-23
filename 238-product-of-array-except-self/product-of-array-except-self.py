

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        zero_idx = []
        mul = 1
        res = [0]*len(nums)
        


        for i in range(len(nums)):

            if nums[i]==0:
                zero_idx.append(i)
            else:
                mul = mul*nums[i]


        if len(zero_idx)==1:
            res[zero_idx[0]] = mul
            return res
        elif len(zero_idx)>1:
            return res
        else:
            for i in range(len(nums)):
                res[i] = mul/nums[i]

            return res























        f = [abs(i) for i in nums]

        mul = 1
        c = 0
        
        for i in nums:
            if i==0:
                c+=1
            else:
                mul = mul*i

        if sum(f)==0 or c>1:
            res = [0 for i in nums]
            return res

        res = []

    
        for i in nums:
            # print(res)
            if c==1:
                if i==0:
                    res.append(mul)
                else:
                    res.append(0)

            else:
                res.append(mul/i)


        return res