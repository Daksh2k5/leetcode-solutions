// Last updated: 8/9/2026, 12:35:45 PM
class Solution {
    public int maxSum(int[][] grid) {
        int prod=Integer.MIN_VALUE;
        for (int i=0;i<grid.length-2;i++){
            for(int j=0;j<grid[0].length-2;j++){
                int n= grid[i][j]+grid[i][j+1]+grid[i][j+2]+grid[i+1][j+1]              +grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2];
                prod=Math.max(n,prod);
            }
        }
        return prod;
    }
}