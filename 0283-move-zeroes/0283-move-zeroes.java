class Solution {
    public void moveZeroes(int[] nums) {
        // int arr[]=new int[nums.length];
        // int index=0;
        // for(int i=0;i<nums.length;i++){
        //     if(nums[i]!=0){
        //         arr[index]=nums[i];
        //         index++;
        //     }
        // }
        int left=0;
        int right=1;
        if(nums.length>1){
        while(right<nums.length){
            if(nums[left]==0){
                if(nums[right]!=0){
                    nums[left]=nums[right];
                    nums[right]=0;
                    
                  right++;
            left++;   
                }
                else{
                   right++;
                }
            }
            else{
                left++;
                right++;
            }
            System.out.print("hello");
           
             
            
        }

    }
    }
}