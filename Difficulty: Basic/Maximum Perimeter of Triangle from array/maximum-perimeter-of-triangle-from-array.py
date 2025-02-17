class Solution:
    def maxPerimeter(self, arr):
        #code here.
        arr.sort()
        for i in range(len(arr)-1,1,-1):
            if arr[i-2]+arr[i-1] >= arr[i]:
                return arr[i]+arr[i-1]+arr[i-2]
        return -1

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        solution = Solution()
        print(solution.maxPerimeter(arr))
        print("~")
# } Driver Code Ends