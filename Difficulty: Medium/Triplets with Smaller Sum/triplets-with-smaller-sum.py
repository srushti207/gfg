class Solution:
    def countTriplets(self, n, sum, arr):
        #code here
        arr.sort()
        result = 0
        
        for i in range(n-2):
            j = i+1
            k = n-1
            
            while j < k:
                val = arr[i] + arr[j] + arr[k]
                if val >= sum:
                    k-=1
                else:
                    result += (k-j)
                    j+=1
        return result
            

#{ 
 # Driver Code Starts
t = int(input())
for _ in range(0, t):
    l = list(map(int, input().split()))
    n = l[0]
    k = l[1]
    a = list(map(int, input().split()))
    ob = Solution()
    ans = ob.countTriplets(n, k, a)
    print(ans)

    print("~")
# } Driver Code Ends