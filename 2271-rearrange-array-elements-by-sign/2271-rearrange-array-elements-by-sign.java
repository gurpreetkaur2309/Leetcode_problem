class Solution {
    public int[] rearrangeArray(int[] nums) {
        int arr[]=new int[nums.length/2];
         int arr1[]=new int[nums.length/2];
         int index=0;
         int temp=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]>0){
                arr[index]=nums[i];
                index++;
            }
            else{
                arr1[temp]=nums[i];
                temp++;
            }

        }
        index=0;
        temp=0;
        int res[]=new int[nums.length];
        for(int i=0;i<nums.length;i++){
           if(i%2==0){
            res[i]=arr[index];
            index++;
           }
           else{
            res[i]=arr1[temp];
            temp++;
           }

        }
        return res;
          
       
        
    }
}