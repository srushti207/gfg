#User function Template for python3

class Solution:
    def findDiff(self, arr):
        # code here
        if not arr:
            return 0
            
        freq = {}
        for i in arr:
            freq[i] = freq.get(i,0)+1
        
        max_freq = max(freq.values())
        min_freq = min(freq.values())
        
        return max_freq - min_freq
    
    
    


#{ 
 # Driver Code Starts
def main():
    T = int(input())

    while T > 0:
        a = list(map(
            int,
            input().strip().split()))  # Convert input to list of integers
        print(Solution().findDiff(a))
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends