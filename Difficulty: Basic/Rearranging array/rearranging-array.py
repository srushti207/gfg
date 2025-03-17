#User function Template for python3

class Solution:    
    def Rearrange(self, arr):
        #Code Here
        arr.sort()
        res = []
        curr = 0
        last = len(arr)-1
        while last > curr:
            res.append(arr[curr])
            curr += 1
            res.append(arr[last])
            last -= 1
        
        if len(arr)%2 != 0:
            res.append(arr[curr])
            
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.Rearrange(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends