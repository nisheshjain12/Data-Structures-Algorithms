class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        m,n=len(image),len(image[0])
        c = image[sr][sc]

        def valid(i,j):
            if i<0 or i>=m:
                return False
            if j<0 or j>=n:
                return False
            return True
        
        def dfs(i,j):
            image[i][j] = color
            if valid(i+1,j) and image[i+1][j] == c:
                dfs(i+1,j)
            if valid(i-1,j) and image[i-1][j] == c:
                dfs(i-1,j)
            if valid(i,j+1) and image[i][j+1] == c:
                dfs(i,j+1)
            if valid(i,j-1) and image[i][j-1] == c:
                dfs(i,j-1)
        
        dfs(sr,sc)
        return image


