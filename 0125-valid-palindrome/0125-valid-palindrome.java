class Solution {
    public boolean isPalindrome(String s) {
        s=s.toLowerCase();
        System.out.println(s);
        String news="";
        for(int i=0;i<s.length();i++){
            if((int)s.charAt(i)>=65 && (int)s.charAt(i)<=90 ||(int)s.charAt(i)>=97 && (int)s.charAt(i)<=122 ||  (int)s.charAt(i)>=48 && (int)s.charAt(i)<=57 ){
               news=news+s.charAt(i); 
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