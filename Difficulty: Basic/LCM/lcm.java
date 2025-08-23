// User function Template for Java
class Solution {
    public static int LCM(int a, int b) {

        // write your code here
        int x = Math.max(a,b);
        int ans = 0;
        for(int i=x;i<=(a*b);i++){
            if(i%a==0 && i%b==0){
                ans=i;
                break;
            }
        }

        // return LCM of a and b
        return ans;
    }
}