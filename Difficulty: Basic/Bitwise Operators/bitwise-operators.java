//Back-end complete function Template for Java
import java.util.Scanner;

public class Solution {
    public static void solve() {
        Scanner scn = new Scanner(System.in);
        int a = scn.nextInt();
        int b = scn.nextInt();
        int c = scn.nextInt();
        // Perform all the operations and print in a single line
        
        int d = a^a;
        int e = c^b;
        e = ~e;
        int f = a&b;
        int g = c|(a^a);
        System.out.println(d+" "+e+" "+f+" "+g);
    }
}