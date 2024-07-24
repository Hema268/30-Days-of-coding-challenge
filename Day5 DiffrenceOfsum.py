#The function accepts two integers n, m as arguments Find the sum of all numbers in range from 1 to m(both inclusive) 
#that are not divisible by n. Return difference between sum of integers not divisible by n with sum of numbers divisible by n.
def diffrenceOfsum(n,m):
    s , s1 = 0
    for i in range(1,m+1):
        if i % n == 0:
            s += i
        else:
            s1 += i
    print(s,s1)
        
    return abs(s1-s)
n = int(input("enter n:"))
m = int(input("enter M:"))
print(diffrenceOfsum(n,m))
