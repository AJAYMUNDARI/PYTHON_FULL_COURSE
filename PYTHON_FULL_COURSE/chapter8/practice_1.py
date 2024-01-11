def great(n1,n2,n3):
    if(n1>n2):
        gtr=n1
    else:
        gtr=n2
    if(gtr<n3):
        gtr=n3
    return gtr

a=great(9,73,12)
print(a)
