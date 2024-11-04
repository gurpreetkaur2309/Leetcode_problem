class Solution {
    public boolean containsDuplicate(int[] nums) {
    //    HashMap<Integer, Integer> hm = new HashMap<>(); 
       
    //    int count=0;
      
    //     for(int i=0;i<nums.length;i++){
            
    //         count=1;
            
    //         if(hm.containsKey(nums[i])){
    //              count++;
    //             hm.put(nums[i],count);
    //         }
    //         else{
    //             hm.put(nums[i],count);
    //         }
    //         // if(nums.length%2!=0){
    //         //     return nums[]
    //         // }
    //     }
    //     if(hm.containsValue(2)){
    //         return true;
    //     }
    //     else{
    //         return false;
    //     }
    
    Arrays.sort(nums);
           for(int i=0;i<nums.length-1;i++){
            if(nums[i]==nums[i+1]){
            
            return true;
            }
            // else{
            //     flag=false;
            // } 
                    
            //  }
            //  if(flag==true){
            //     return true;
            //  }
            //  else{
            //     return false;
            //  }
           
}
    return false;   
     
        
    } 
}
    
