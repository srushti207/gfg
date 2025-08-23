class Solution {
    public void printEvenIndices(String s) {
        // code here
        String ans = "";
        for(int i=0;i<=s.length();i++){
            if(i%2 == 0){
                System.out.print(s.charAt(i));
            }
        }
        
    }
}