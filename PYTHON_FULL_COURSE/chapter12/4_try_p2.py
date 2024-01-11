a=9
def func():
    global a
    a=8
    print(a)
    a=99
    print(a)

print(a)            #print parent value of a that is 9
func()
print(a)            #after decalring global keyword, parent value of a will changed
