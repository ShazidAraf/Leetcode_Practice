class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        m,n = len(board), len(board[0])

        MASK = []

        for i in range(len(board)):
            arr = [0 for j in range(len(board[0]))]
            MASK.append(arr)


        def search(mask,p,q,l):

            if l==len(word):
                return True
            
            if p<0 or q<0 or p>m-1 or q>n-1:
                return False

            if board[p][q]!=word[l] or mask[p][q]==1:
                return False

            else:
                mask[p][q] = 1

                found =  search(mask,p+1,q,l+1) or search(mask,p-1,q,l+1) or search(mask,p,q+1,l+1) or search(mask,p,q-1,l+1)
                mask[p][q] = 0

                return found


        for i in range(m):  
            for j in range(n):
                if search(MASK,i,j,0):
                    return True
        return False