
class Solution {
    public double[] FindRoots(int A, int B, int C) {
        // code here
        double a = (B*B-4*A*C);
        double b = Math.sqrt(a);
        double c = (-(1*B)+b)/(2*A);
        double c1 = (-(1*B)-b)/(2*A);
        if(a<0) return new double[]{-1};
        double[] root = new double[2];
        if(c>c1){
            root[0] = c1;
            root[1] = c;
        }else{
            root[0] = c;
            root[1] = c1;
        }
        return root;
    }
}