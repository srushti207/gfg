// User function Template for Java
class Solution {
    static ArrayList<Integer> getSum(int N) {
        // code here
        ArrayList<Integer> array = new ArrayList<>();
        int sumeven = 0;
        int sumodd = 0;
        for(int i=0;i<=N;i++){
            if(i%2 == 0){
                sumeven += i;
            }else{
                sumodd += i;
            }
        }
        array.add(sumeven);
        array.add(sumodd);
        return array;
    }
}