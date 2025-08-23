// User function Template for Java
class Solution {
    public static int nFactorial(int n) {
        int ans = 1;

        // Write your code here
        if(n==0){
            return 1;
        }
        return n*nFactorial(n-1);
    }
}