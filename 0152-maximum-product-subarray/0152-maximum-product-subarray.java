class Solution {
    public int maxProduct(int[] arr) {
         int max=arr[0];
        for(int i=0;i<arr.length;i++){
            int prod=1;
            for(int j=i;j<arr.length;j++){
                prod=prod*arr[j];
                 if(prod>max){
                     max=prod;
                 }
            }
        }
        return max;
        
    }
}