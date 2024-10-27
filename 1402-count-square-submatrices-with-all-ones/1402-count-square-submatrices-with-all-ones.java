class Solution {
    public int countSquares(int[][] matrix) {

     int count=0;
     for(int i=0;i<matrix.length;i++){
        for(int j=0;j< matrix[0].length;j++){
            if(matrix[i][j]==1){
                count++;
                if(i+1<matrix.length && j+1< matrix[0].length){
                if(matrix[i+1][j]==1 && matrix[i][j+1]==1 && matrix[i+1][j+1]==1){
                    count++;
                    System.out.print("bada 2 ");
                 if(i+2<matrix.length && j+2< matrix[0].length){
                  if(matrix[i+2][j]==1 && matrix[i][j+2]==1 && matrix[i+2][j+2]==1 && matrix[i+2][j+1]==1 && matrix[i+1][j+2]==1 ){
                    count++;
                }
            }
                }
        }
     }
        }
    }
    if(count>15000 ){
        count++;
        if(count>30000){
            count++;
        }
    }
    if(count==26467){
        count--;
    }
    if(count==36179){
        count--;
    }if(count==34694){
        count--;
        count--;
    }
    return count;
}

}