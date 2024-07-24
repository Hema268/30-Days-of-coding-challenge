def operation(s):
    a = int(s[0])
    i = 1
    while i < len(s):
        if s[i] == 'A':
            a &= int(s[i+1])
        elif s[i] == 'B':
            a |= int(s[i+1])
        else:
            a ^= int(s[i+1])
        i += 2
    return a
s = "0C1A1B1C1C1B0A0"
print(operation(s))
