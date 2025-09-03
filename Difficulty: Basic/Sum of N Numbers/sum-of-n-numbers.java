// User function Template for Java
class Solution {
    public int sumOfNumbers(int n) {
        // code here
        int sum1 = 0;
        while(n>0){
            sum1 += n;
            n-=1;
        }
        return sum1;
    }
}