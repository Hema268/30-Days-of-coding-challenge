def check_password(p,n):
    if n < 4 and p[0].isdigit():
        return 0 
    cap = 0
    num = 0
    for i in range(n):
        if p[i] == " " or p[i] == '/':
            return 0
        if p[i] >= 'A' and p[i] <= 'Z':
            cap += 1
        elif p[i].isdigit():
            num += 1
    if cap > 0 and num > 0:
        return 1
    else:
        return 0
        
p = input("Enter password: ")
n = len(p)
print(check_password(p,n)) 
