// class Solution {
//     public String longestCommonPrefix(String[] strs) {
//         int temp=0;
//         char ch;
//         String out;
//         String s[]=new String[strs.length];
//         Arrays.sort(s);
        
//         for(int i=0;i<strs.length ;i++){
//             // for(int j=0;j<strs[i].length();j++){
//                 if(temp>0){
//                     if(ch==strs[i].charAt(temp)){
//                         if(temp==strs.length-1){
//                         out.add(ch);
//                         temp++;
//                         }
//                         continue;
//                     }
//                 }
//                 ch=strs[i].charAt(temp);
//             // }
//         }
//     }
// }
class Solution {
    public String longestCommonPrefix(String[] strs) {
        Arrays.sort(strs);
        String s1 = strs[0];
        String s2 = strs[strs.length-1];
        int idx = 0;
        while(idx < s1.length() && idx < s2.length()){
            if(s1.charAt(idx) == s2.charAt(idx)){
                idx++;
            } else {
                break;
            }
        }
        return s1.substring(0, idx);
    }
}