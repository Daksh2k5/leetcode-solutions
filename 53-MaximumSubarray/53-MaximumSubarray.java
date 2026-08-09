// Last updated: 8/9/2026, 12:37:45 PM
class Solution {
    public int maxSubArray(int[] nums) {
        int sum=Integer.MIN_VALUE;
        int s=0;
        for (int i=0;i< nums.length;i++){
            
                s=s+nums[i];
                sum=Math.max(sum,s);      
                if(s<0){
                    s=0;
                }         
            
        }
        return sum;
    }
}