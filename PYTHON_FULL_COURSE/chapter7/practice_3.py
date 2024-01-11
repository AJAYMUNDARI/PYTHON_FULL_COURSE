#to searchb a word using while loop
l1=["ajay","mosee","bjju","rahul","kiran"]
i=0
while(i<len(l1)):
    item=l1[i]
    if item.startswith("a"):
        print(f"good morning {item}")
    i+=1