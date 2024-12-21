#User function Template for python3

class Solution:
    def sortedCount(self,N,M,Mat):
        #code here
        count = 0
        for i in Mat:
            if len(i) == 1:
                count += 1
            else:
                inc = 0
                dec = 0
                for j in range(0,M-1):
                    if i[j]>i[j+1]:
                        dec += 1
                    elif i[j]<i[j+1]:
                        inc += 1
                    else:
                        break
                    
                if inc==M-1 or dec==M-1:
                    count+=1
                    
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        Mat=[]
        for i in range(N):
            Mat.append(list(map(int,input().strip().split(" "))))
        ob=Solution()
        ans=ob.sortedCount(N,M,Mat)
        print(ans) 
        print("~")
# } Driver Code Ends