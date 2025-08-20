// User function Template for Java

class Solution {
    static double switchCase(int choice, List<Double> arr) {
        // code 
        double ans = 0.0;
        switch(choice){
            case 1: 
                double R = arr.get(0);
                ans = Math.PI*R*R;
                break;
            case 2:
                double L = arr.get(0);
                double B = arr.get(1);
                ans = L*B;
                break;
            default: break;
        }
        return ans;
        
    }
}