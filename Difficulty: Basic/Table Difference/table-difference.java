// User function Template for Java
class Solution {
    public static void difference(int n1, int n2) {

        // Write your code here
        for(int i=1;i<11;i++){
            int ans = (n1*i) - (n2*i);
            System.out.print(ans+ " ");
        }
    }
}