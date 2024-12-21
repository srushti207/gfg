#User function Template for python3

class Solution:
    def factorial(self, n):
        #code here
        if n == 0 and n == 1:
            return [0]
            
        fact = 1
        for i in range(2,n+1):
            fact *= i
            
        digit = [int(digit) for digit in str(fact)]
        
        return digit


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorial(N)
        print(" ".join(
            str(i) for i in
            ans))  # Join each digit to form the full number without spaces
        print("~")

# } Driver Code Ends