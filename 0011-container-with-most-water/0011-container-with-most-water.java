class Solution {
    public int maxArea(int[] height) {
        // int max=0;
        // int h=0;
        // int area=0;
        // for(int i=0;i<height.length-1;i++){
        //     for(int j=i+1;j<height.length;j++){
        //       int breadth=j-i;
        //       if(height[i]<height[j]){
        //          h=height[i];
        //       }
        //       else{
        //         h=height[j];
        //       }
        //        area=h*breadth;
        //       if(area>max){
        //         max=area;
        //       }
        //     System.out.print(max);
        //     }
        // }
        // return max;
        int left=0;
        int right=height.length-1;
        int max=0;
        int width=0;
        int h=0;
        while(left<right){
            width=right-left;
            if(height[left]<height[right]){
             h=height[left];
            }
            else{
              h=height[right];  
            }
            if(h*width>max){
                max=h*width;
            }
            if(height[left]<height[right]){
                left++;
            }
            else{
            right--;
            }
            
        }
        return max;
    }
}