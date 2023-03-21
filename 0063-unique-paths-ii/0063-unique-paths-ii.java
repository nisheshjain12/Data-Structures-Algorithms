class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        
        if(  obstacleGrid[(obstacleGrid.length)-1][(obstacleGrid[0].length)-1] == 1 ) return 0;
        
        int dp[][] = new int[obstacleGrid.length][obstacleGrid[0].length];
        
        for(int arr[]: dp)
        Arrays.fill(arr,-1);
        
        return helper(0,0,obstacleGrid,dp);
    }
    public int helper(int i,int j,int obstacleGrid[][],int dp[][]){
        
        if( i==(obstacleGrid.length) ||  j==(obstacleGrid[0].length)) return 0;
        
        if(  obstacleGrid[i][j] == 1  ) dp[i][j] = 0;
        
        if(i==(obstacleGrid.length)-1 && j==(obstacleGrid[0].length)-1 ) return 1;
        
       
        
        if (dp[i][j] != -1 ) return dp[i][j];
        
        dp[i][j] = helper(i+1,j,obstacleGrid,dp)+helper(i,j+1,obstacleGrid,dp);
        return dp[i][j];
    }
}