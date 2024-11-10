class Solution {
    public int removeDuplicates(int[] nums) {
      
        int count=1;
      ArrayList<Integer> arr=new ArrayList<>();
      arr.add(nums[0]);
      if(nums.length>1){
      for(int i=1;i<nums.length;i++){
        int flag=1;
        for(int k=0;k<arr.size();k++){
            if(nums[i]==arr.get(k)){
                flag=0;
                break;
            }
        }
         if(flag==1){
            System.out.print(nums[i]);
           arr.add(nums[i]); 
          
        }
           
        
      } 
      }
      int temp=0;
      while(temp<arr.size()){
        nums[temp]=arr.get(temp);
        temp++;
      }

      
    return arr.size();

    }
}