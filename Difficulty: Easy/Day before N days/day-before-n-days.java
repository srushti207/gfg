// User function Template for Java
class Solution {
    public static int nthDay(int d, int n) {
        // write your code here
        int ans = d-n%7;
        return (ans+7)%7;
        
    }
}