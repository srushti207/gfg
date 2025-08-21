class Complete {
    public static ArrayList<Integer> array(int a[][], int b[], int n) {
        // Complete the function
        int sum = 0;
        int greater = 0;
        ArrayList<Integer> arr = new ArrayList<>();
        
        for(int i=0; i<n; i++){
            for(int j=0;j<n;j++){
                if(i==j){
                    sum += a[i][j];
                }
            }
        }
        for(int k=0;k<b.length;k++){
            if(greater<b[k]){
                greater = b[k];
            }
        }
        arr.add(sum);
        arr.add(greater);
        return arr;
    }
}
