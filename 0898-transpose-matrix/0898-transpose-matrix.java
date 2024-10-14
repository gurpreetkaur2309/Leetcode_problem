
        class Solution {
    public int[][] transpose(int[][] matrix) {
       int sum[][]=new int[matrix[0].length][matrix.length];
       int temp=0;
       for(int i=0;i<matrix.length;i++){
        for(int j=0;j<matrix[0].length;j++){
           temp=matrix[i][j];
           
            int r=i;
            int s=j;
            sum[s][r]=temp;
          
        }
       } 
       
       return sum;
    }
}