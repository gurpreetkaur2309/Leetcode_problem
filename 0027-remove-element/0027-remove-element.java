class Solution {
    public int removeElement(int[] nums, int val) {
       int count=0;
      ArrayList<Integer> arr = new ArrayList<Integer>();
      for(int i=0;i<nums.length;i++){
        if(nums[i]==val){
            count++;
        }
        else{
            arr.add(nums[i]);
        }
      } 
    //   int a=nums.length-count;
    //   int arr[]=new int[a];
      for(int i=0;i<arr.size();i++){
        int k=arr.get(i);
        nums[i]=k;
      }
      return (nums.length-count);  
    }
}