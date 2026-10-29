class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        a = sum(gas)
        b = sum(cost)

        if a<b:
            return -1

        running_sum = 0
        start = False
        index = None

        for i in range(len(gas)):

            if start==False and cost[i]>gas[i]:
                    continue

            start = True

            if index is None:
                index = i
            running_sum += gas[i]-cost[i]
            
            if running_sum <0:
                start = False
                index = None
                running_sum = 0

        return index



            

        
        