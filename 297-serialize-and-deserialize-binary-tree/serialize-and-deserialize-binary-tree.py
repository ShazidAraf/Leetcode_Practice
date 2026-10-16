# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        res = []
        q = collections.deque([root])

        while q:

            for _ in range(len(q)):
                node = q.popleft()

                if node:
                    res.append(str(node.val))
                    q.append(node.left)
                    q.append(node.right)
                else:
                    res.append("%")

        # print(res)
        return ','.join(res)

        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        

        data = data.split(',')
        print(data)

        if data[0]=='%':
            return None
        

        root = TreeNode(int(data[0]))
        q = collections.deque([root])
        i = 1

        while q:

            for _ in range(len(q)):

                node = q.popleft()

                if data[i]!="%":

                    p = TreeNode(int(data[i]))
                    node.left = p
                    q.append(p)
                i+=1

                if data[i]!="%":
                    p = TreeNode(int(data[i]))
                    node.right = p
                    q.append(p)
                i+=1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))