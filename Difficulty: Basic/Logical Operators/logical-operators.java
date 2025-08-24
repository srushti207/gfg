class Solution {
    public String booleanOperations(boolean a, boolean b) {
        // Code here
        boolean ans1 = a&&b;
        boolean ans2 = a||b;
        boolean ans3 = !a;
        return ans1+" "+ans2+" "+ans3;
        // System.out.println(ans1+" "+ans2+" "+ans3);
    }
}