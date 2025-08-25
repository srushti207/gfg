// User function Template for Java

class Solution {
    public static ArrayList<Integer> commonElements(int a[], int b[]) {
        // Your code here
        Arrays.sort(a);
        Arrays.sort(b);
        ArrayList<Integer> result = new ArrayList<>();
        HashMap<Integer, Integer> h1 = new HashMap<>();
        
        for(int arr:a){
            h1.put(arr,h1.getOrDefault(arr,0)-1);
        }
        Arrays.sort(b);
        for(int brr:b){
            h1.put(brr,h1.getOrDefault(brr,0)+1);
            if(h1.get(brr)<=0){
                result.add(brr);
            }
        }
        return result;
    }
}