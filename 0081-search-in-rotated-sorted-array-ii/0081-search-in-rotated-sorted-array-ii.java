class Solution {
    public boolean search(int[] nums, int target) {
        boolean temp=false;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==target){
                temp=true;
            }
        }
        return temp;
    }
}