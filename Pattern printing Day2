#Day 2 Pattern printing
def printPat(n):
    #Code herefor 
    for i in range(n,0,-1):
        for j in range(n,0,-1):
            print((str(j)+" ")*i,end="")
        print("$",end="")

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        printPat(n)
        print()

#Rectangle pattern
def rect(a,b):
    for row in range(a):
        if row == 0 or row == a-1:
            print("*" * b)
        else:
            print("*" + ' ' * (b-2) + "*")
rect(4,6)
rect(6,20)
