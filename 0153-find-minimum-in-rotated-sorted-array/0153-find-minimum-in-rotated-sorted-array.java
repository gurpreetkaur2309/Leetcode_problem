class Solution {
    public int findMin(int[] arr) {
        int count=arr[0];
        if(arr.length>1){
        // if(arr[0]>arr[1]){
        //     for(int i=1;i<arr.length-1;i++){
        //     if(arr[i]<arr[i+1]){
        //         count=arr[i+1];
        //        return arr[i+1];

        //     }
        //   }
        // }
        // else{
        //      for(int i=1;i<arr.length-1;i++){
        //     if(arr[i]>arr[i+1]){
        //         count=arr[i+1];
        //        return arr[i+1];
        //     }
        //   }
        // }
        // } 
        for(int i=1;i<arr.length;i++){
            if(arr[i]<count)
            count=arr[i];
        }
        }
        return count;
    }
}