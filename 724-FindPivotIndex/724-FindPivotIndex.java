// Last updated: 8/9/2026, 12:36:19 PM
class Solution {
    public int pivotIndex(int[] nums) {

        for(int i=0;i<nums.length;i++){
            int suml=0;
            int sumr=0;
            for(int l=0;l<i;l++){
                suml=suml+nums[l];
            }
            for(int r=i+1;r<nums.length;r++){
                sumr=sumr+nums[r];
            }
            if(sumr==suml){
                return i;
            }

        }
        return -1;
    }
}