

class Solution {
    static ArrayList<Integer> javaIterator(int n, int k, int[] arr) {
        // code here
        ArrayList<Integer> res = new ArrayList<>();
        Arrays.sort(arr);
        for(int i:arr){
            if(i>=k){
                res.add(i);
            }
        }
        return res;
    }
};