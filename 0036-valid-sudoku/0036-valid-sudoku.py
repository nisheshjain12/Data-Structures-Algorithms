class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            vis=set()
            for j in range(9):
                if board[i][j] !='.':
                    if board[i][j] not in vis:
                        vis.add(board[i][j])
                    else:
                        return False
                
        for i in range(9):
            vis=set()
            for j in range(9):
                if board[j][i] !='.':
                    if board[j][i] not in vis:
                        vis.add(board[j][i])
                    else:
                        return False
                    
        squareSet = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] =='.': 
                    continue
                sr, sc = i // 3, j // 3
                sPos = sr + sc*3
                if board[i][j] in squareSet[sPos]:
                    return False
                squareSet[sPos].add(board[i][j])
                
        return True