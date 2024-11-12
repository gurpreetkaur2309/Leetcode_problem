class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int index=nums[0];
        int count=0;
        ArrayList<Integer> arr=new ArrayList<>();
       
            // if(nums.length==0){
            //     return 0;
            // }
            // if(nums[0]==1){
            //     return 1;
            // }
            // else{
            //     return 0;
            // }
        
       
        for(int i=0;i<nums.length;i++){
            index=nums[i];
            if(index==1){
             
             
             count++;
             System.out.print(count+"if");
            }
            else{
                
                count=0;
                System.out.print(count+"wlse");
                
            }
            arr.add(count);
            
        }
        if(arr.size()>=1){
        int max=arr.get(0);
        for(int i=1;i<arr.size();i++){
            System.out.print(arr.get(i));
            if(arr.get(i)>max){
                max=arr.get(i);
            }
        }
        count=max;
        return max;
        }
        return count; 
    }
}