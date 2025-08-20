class Solution {
    public int lastDigit(int n) {
        // Code here
        int ans = n%10;
        return Math.abs(ans);
    }
}