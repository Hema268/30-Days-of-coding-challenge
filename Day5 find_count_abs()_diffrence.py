#The function accepts an integer array ‘arr’, its length and two integer variables ‘num’ and ‘diff’. Implement this function 
#to find and return the number of elements of ‘arr’ having an absolute difference of less than or equal to ‘diff’ with ‘num’.

arr = list(map(int,input("Enter the Array: ").split()))
num = int(input("Enter num : "))
diff = int(input("Enter diffrence: "))
n = len(arr)
c = 0
for i in range(n):
    a  = abs(arr[i] - num)
    if a <= diff:
        c += 1
print(c)
