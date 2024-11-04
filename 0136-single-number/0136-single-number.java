class Solution {
    public int singleNumber(int[] nums) {
      HashMap<Integer, Integer> hm = new HashMap<>(); 
       
       int count=0;
      
        for(int i=0;i<nums.length;i++){
            
            count=1;
            
            if(hm.containsKey(nums[i])){
                 count++;
                hm.put(nums[i],count);
            }
            else{
                hm.put(nums[i],count);
            }
            // if(nums.length%2!=0){
            //     return nums[]
            // }
        }
        for (int i : hm.keySet()) {
  System.out.println("key: " + i + " value: " + hm.get(i));
  if(hm.get(i)==1){
    return i;
  }
}
        System.out.print(hm);
        return 0;
        
    }
}