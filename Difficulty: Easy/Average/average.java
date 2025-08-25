class Solution {
    public static double posAverage(int[] arr) {
        // Code here
        double sum = 0;
        int cnt = 0;
        for(int i=0;i<arr.length;i++){
            if(arr[i]>=0){
                cnt += 1;
                sum += arr[i];
            }
        }
        return (sum/cnt);
    }
}
