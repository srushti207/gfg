#User function Template for python3

class Solution:
    def minRow(self,a):
        #code here
        n = len(a)
        min_one = float('inf')
        indx = 1
        
        for i in range(n):
            ones = sum(a[i])
            if min_one > ones:
                min_one = ones
                indx = i+1
        return indx


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        M = int(input())
        mat = []
        for i in range(N):
            B = list(map(int, input().strip().split(" ")))
            mat.append(B)
        ob = Solution()
        print(ob.minRow(mat))
        print("~")

# } Driver Code Ends