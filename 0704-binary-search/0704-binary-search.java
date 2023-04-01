class Solution {
    public int search(int[] nums, int target) {
        int n=nums.length;
        int low=0;
        int high=n-1;
        int mid=(low+high)/2;
        while(low<=high){
            if(nums[mid] == target) return mid;
            if(nums[mid] > target) high=mid-1;
            if(nums[mid] < target) low=mid+1;
            mid=(low+high)/2;
        }
        return -1;
    }
}