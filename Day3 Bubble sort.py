#User function Template for python3

class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        # code here
        for i in range(0,n-1):
            for j in range(0,n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        return arr
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.bubbleSort(arr, n)
        for i in arr:
            print(i,end=' ')
        print()

# } Driver Code Ends
# ANOTHER METHOD TO SLOVE BUBBLE SORT
a = [8,3,5,2,1]
for i in range(0,5):
    for j in range(i+1,5):
        if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]
print(a)
