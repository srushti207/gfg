#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
class Solution:

	def nextGreatest(self,arr):
		# code  here
		n = len(arr)
		mx = -1
		for i in range(n-1,-1,-1):
		    arr[i], mx = mx, max(arr[i],mx)
		return arr

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.nextGreatest(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends