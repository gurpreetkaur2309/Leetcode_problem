class Solution {
    public int search(int[] arr, int target) {
        int temp=-1;
        for(int i=0;i<arr.length;i++){
            if(arr[i]==target){
                temp=i;
            }
        }
        return temp;
    }
}