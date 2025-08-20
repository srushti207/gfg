class Solution {
    public static void utility(String s) {
        // code here
        int n = s.length();
        for(int i=0;i<n;i++){
            if(i%2 == 0){
                System.out.print(s.charAt(i));
            }
        }
        
    }
}