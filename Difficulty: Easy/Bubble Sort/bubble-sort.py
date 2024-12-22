#User function Template for python3

class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr):
        # code here
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            
            if swapped == False:
                break
        
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):

        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.bubbleSort(arr)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends