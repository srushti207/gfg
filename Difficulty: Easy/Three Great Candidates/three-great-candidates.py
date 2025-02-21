#User function Template for python3

class Solution:
    def maxProduct(self, arr):
        # code here
        n = len(arr)
        arr.sort()
        
        return max(arr[0]*arr[1]*arr[n-1], arr[n-1]*arr[n-2]*arr[n-3])

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1
        print("~")
# } Driver Code Ends