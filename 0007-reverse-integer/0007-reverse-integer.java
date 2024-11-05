class Solution {
    public int reverse(int x) {
       
        int num=x;
        int rem=0;
        int prod=0;
        if(x<0){
            num=-x;
        }
        
        while(num>0){
         rem=num%10;
         if(prod>((2147483647-rem)/10)
){  return 0;
        }
         prod=prod*10+rem;
         num=num/10;
        }
         
        if(x<0){
            return -prod;
        }
        
        return prod;
        
    }
}