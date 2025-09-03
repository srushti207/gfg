// User function Template for Java

class Solution {
    public static int max_toys(int arr[], int k) {
        // Your code here
        int cnt = 0;
        int sum = 0;
        Arrays.sort(arr);
        for(int i=0;i<arr.length;i++){
            sum += arr[i];
            if(k>=sum){
                cnt ++;
            }
        }
        return cnt;
    }
}