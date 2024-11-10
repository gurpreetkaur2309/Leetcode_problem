class Solution {
    public boolean check(int[] nums) {
    int arr[]=new int[nums.length];
    for(int i=0;i<nums.length;i++){
         arr[i]=nums[i];
        }

        Arrays.sort(nums);
        
        int flag=1;
        for(int i=0;i<nums.length;i++){
            if(arr[i]!=nums[i]){
               flag=0;
               break;
            }
            
        }
        if(flag==1){
            return true;
        }
        else{
        for(int x=1;x<nums.length;x++){
            flag=1;
        for(int i=0;i<nums.length;i++){
           
            if(nums[i] != arr[(i+x) % arr.length]){
                flag=0;
                break;
            }         
        }
        if(flag==1){
            return true;
        }


        }
        }
        return false;
    }
}