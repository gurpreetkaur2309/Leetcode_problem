class Solution {
    public int missingNumber(int[] nums) {
        // Arrays.sort(nums);
        int flag=1;
        for(int i=0;i<=nums.length;i++){
            flag=0;
            for(int j=0;j<nums.length;j++){
                if(i==nums[j]){
                    flag=1;
                }
            }
            // if(nums[i+1]-nums[i]!=1){
            //     return nums[i]+1;
            // }
            // else{
            //     flag=0;
            // }
            if(flag==0){
                return i;
            }
        }
      
        
        return 0;
        
        
    }
}