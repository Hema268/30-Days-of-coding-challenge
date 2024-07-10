#Day 2
#Palindromic Array
def PalinArray(arr):
    # Code here
    def pal(i):
        i = str(i)
        return i == i[::-1]
    a = all(pal(i) for i in arr)
    return a

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr):
            print("true")
        else:
            print("false")

#Palindrome
class Solution:
	def is_palindrome(self, n):
		# Code here
		a = str(n)
		if  a == a[::-1]:
		    return "Yes"
		else:
		    return "No"

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.is_palindrome(n)
		print(ans)
