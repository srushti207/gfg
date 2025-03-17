# User function Template for Python 3

class Solution:
    def printMinimumProduct(self, a):
        # code here
        a.sort()
        
                
        return a[0]*a[1]
    
    


#{ 
 # Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())

    while T > 0:
        a = list(map(
            int,
            input().strip().split()))  # Convert input to list of integers
        print(Solution().printMinimumProduct(a))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends