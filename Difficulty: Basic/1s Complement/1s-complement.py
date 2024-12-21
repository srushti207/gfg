#User function Template for python3
class Solution:
    def onesComplement(self,S,N):
        # code here
        a = str(S)
        f=""
        for i in a:
            if i=='0':
                f+='1'
            else:
                f+='0'
        return f


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        S = input()

        ob = Solution()
        print(ob.onesComplement(S,N))
        print("~")
# } Driver Code Ends