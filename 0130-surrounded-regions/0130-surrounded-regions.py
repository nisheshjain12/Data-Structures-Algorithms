class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])

        def dfs1(i,j):
            if i<0 or j<0 or i>=m or j>=n or board[i][j] != 'O':
                return
            board[i][j] = 'T'
            dfs1(i+1,j)
            dfs1(i-1,j)
            dfs1(i,j+1)
            dfs1(i,j-1)

        for i in range(m):
            for j in range(n):
                if i*j == 0 or i==m-1 or j==n-1 and board[i][j] == 'O' :
                    dfs1(i,j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'














