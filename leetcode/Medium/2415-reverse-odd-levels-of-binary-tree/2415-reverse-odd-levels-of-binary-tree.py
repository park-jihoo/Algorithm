# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q, ans, arr = deque([root]), 0, []
        while q: 
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left: 
                    if ans %2 == 0:
                        arr.append(curr.left.val)
                        arr.append(curr.right.val)  
                    else:
                        curr.val = arr[-1]
                        arr.pop()
                    q.append(curr.left)
                    q.append(curr.right)
                elif curr and arr: 
                    curr.val = arr[-1]
                    arr.pop()
            ans += 1
        return root 