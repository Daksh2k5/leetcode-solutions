// Last updated: 8/9/2026, 12:36:44 PM
class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int m= n*(n+1)/2;
        int sum=0;

        for (int i=0; i<n;i++){
            sum+=nums[i];
        }
        return m-sum;
    }
}