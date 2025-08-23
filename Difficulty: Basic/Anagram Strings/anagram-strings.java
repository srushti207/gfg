// User function template for Java
class Solution {
    static int areAnagram(String S1, String S2) {
        // code here
        if(S1.length() != S2.length()){
            return 0;
        }
        char[] arr1 = S1.toCharArray();
        char[] arr2 = S2.toCharArray();
        Arrays.sort(arr1);
        Arrays.sort(arr2);
        if(Arrays.equals(arr1,arr2)){
            return 1;
        }else{
            return 0;
        }
    }
}