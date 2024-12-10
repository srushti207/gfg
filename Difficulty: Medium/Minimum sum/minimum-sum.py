#User function Template for python3

class Solution:
    def minSum(self, arr):
        # code here
        arr.sort()
        num1 = ""
        num2 = ""
        res = ""
        n = len(arr)
        for i in range(n):
            if i%2 == 0:
                num1 += str(arr[i])
            else:
                num2 += str(arr[i])
                
        carry = 0
        i = len(num1)-1
        j = len(num2)-1
        
        while i>=0 or j>=0 or carry:
            n1 = int(num1[i]) if i>=0 else 0
            n2 = int(num2[j]) if j>=0 else 0
            
            total = n1 + n2 + carry
            carry = total // 10
            res += str(total%10)
            
            i-=1 
            j-=1
        res = res[::-1]
        return res.lstrip('0')

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.minSum(arr)
        print(ans)
        tc -= 1

        print("~")

# } Driver Code Ends