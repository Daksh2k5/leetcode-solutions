// Last updated: 8/9/2026, 12:36:58 PM
class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k=k%n;
        nums=reverse(nums,0,n-1);
        nums=reverse(nums,0,k-1);
        nums=reverse(nums,k,n-1);
    }
        public static int[] reverse(int[] arr, int start, int end) {
        while (start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
        return arr;
    }
}