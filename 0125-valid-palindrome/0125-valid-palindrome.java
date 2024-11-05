// class Solution {
//     public boolean isPalindrome(String s) {
//         s=s.toLowerCase();
//         System.out.println(s);
       
//         // for(int i=0;i<s.length();i++){
//         //     char ch=s.charAt(i);
//         //     if(ch>='a'&& ch<='z' || ch>='A' && ch<= 'Z' || ch>='0' && ch<='9' ){
//         //        news=news+ch; 
//         //     }
//         // }
//         // char left=news.charAt(0);
//         // char right=news.charAt(s.length()-1);
        
//         int left=0;
//         int right=s.length()-1;
//         System.out.print(s);
//         while(left<right){
//             char ch=s.charAt(left);
           
//             if(ch>='a'&& ch<='z' || ch>='A' && ch<= 'Z' || ch>='0' && ch<='9' ){
//               left++; 
//               continue;
//             }




//             if(s.charAt(left)==s.charAt(right)){
//                 left++;
//                 right--;
//             }
//             else{
//                 return false;
//             }
//         }
//         // if()
        
//        return true; 
//     }
// }
class Solution {
    public boolean isPalindrome(String s) {
        
        
        int start = 0, end = s.length()-1;
        
        while(start<end) {
            Character sc = getValid(s.charAt(start));
            if(sc==null) {
                ++ start;
                continue;
            }
            Character ec = getValid(s.charAt(end));
            if(ec==null) {
                --end;
                continue;
            }
            if(sc!=ec) return false;
            ++start;
            --end;
        }
        return true;
    }
    
    private Character getValid(char c) {
        if(c>='a' && c<='z') return c;
        if(c>='A' && c<='Z') return (char) (c + ('a'- 'A'));
        if(c>='0' && c<='9') return c;
        return null;
    }
    
}