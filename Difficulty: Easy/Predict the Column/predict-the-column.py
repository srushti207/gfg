#User function Template for python3

class Solution:
    def columnWithMaxZeros(self,arr,N):
        # code here 
        max_z = []
        
        for i in range(N):
            count = 0
            for j in range(N):
                if arr[j][i] == 0:
                    count += 1
            if count > 0:
                max_z.append(count)
            else:
                max_z.append(-1)
        if len(max_z) > 0 and set(max_z) != {-1}:
            return max_z.index(max(max_z))
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = []
        for i in range(N):
            line = [int(x) for x in input().strip().split()]
            arr.append(line)
        ob=Solution()
        print(ob.columnWithMaxZeros(arr,N))


        print("~")
# } Driver Code Ends