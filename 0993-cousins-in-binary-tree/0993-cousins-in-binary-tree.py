class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return True
        xp,xd=None,-1
        yp,yd=None,-2
        
        def dfs(node,depth,parent):
            nonlocal xp,xd,yp,yd
            if not node:
                return 
            elif node.val == x:
                xp=parent
                xd=depth
            elif node.val == y:
                yp=parent
                yd=depth
            else:
                dfs(node.right,depth+1,node)
                dfs(node.left,depth+1,node)
            
        dfs(root,0,None)
        print(xp, yp, xd,yd)
        if xp!=yp and xd==yd:
            return True
        return False