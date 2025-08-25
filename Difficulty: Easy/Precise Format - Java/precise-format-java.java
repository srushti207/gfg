class Solution {
    // Function to return an ArrayList with exact result and formatted result
    static ArrayList<Float> divisionWithPrecision(float a, float b) {
        // code here
        ArrayList<Float> result = new ArrayList<>();
        float val = a/b;
        float val1 = Math.round(val*1000)/1000.0f;
        result.add(val);
        result.add(val1);
        return result;
        
    }
}