// User function Template for Java

class Solution {
    static int map(int n, String keys[], int arr[], String s) {
        // code here
        HashMap <String,Integer> d = new HashMap<>();
        for(int i=0; i<n; i++){
            d.put(keys[i],arr[i]);
        }
        return d.getOrDefault(s,-1);
    }
}