class Solution {
    public boolean isPalindrome(String s) {
        s=s.toLowerCase();
        System.out.println(s);
        String news="";
        for(int i=0;i<s.length();i++){
            char ch=s.charAt(i);
            if(ch>='a'&& ch<='z' || ch>='A' && ch<= 'Z' || ch>='0' && ch<='9' ){
               news=news+ch; 
            }
        }
        // char left=news.charAt(0);
        // char right=news.charAt(s.length()-1);
        int left=0;
        int right=news.length()-1;
        System.out.print(news);
        while(left<right){
            if(news.charAt(left)==news.charAt(right)){
                left++;
                right--;
            }
            else{
                return false;
            }
        }
        // if()
        
       return true; 
    }
}