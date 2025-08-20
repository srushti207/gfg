class Solution {
    public int[] computeOperations(int x, int y) {
        // code here
        int add = x+y;
        int sub = x-y;
        int mul = x*y;
        int div = x/y;
        int mod = x%y;
        int[] arr = {add,sub,mul,div,mod};
        return arr;
    }
}
