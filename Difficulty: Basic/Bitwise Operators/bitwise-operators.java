class Solution {
    public static void operators(int a, int b, int c) {
        // code here
        int d = a^a;
        int e = c^b;
        e = ~e;
        int f = a&b;
        int g = c | (a^a);
        System.out.println(d+" "+e+" "+f+" "+g);
        
    }
}
