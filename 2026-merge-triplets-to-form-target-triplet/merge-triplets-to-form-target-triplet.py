class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """


        count = set()

        for i in range(len(triplets)):

            trip = triplets[i]

            if trip[0]>target[0] or trip[1]>target[1] or trip[2]>target[2]:
                continue

            if trip[0]==target[0]:
                count.add(0)
            if trip[1]==target[1]:
                count.add(1)
            if trip[2]==target[2]:
                count.add(2)

        if len(count)==3:
            return True
        else:
            return False

        