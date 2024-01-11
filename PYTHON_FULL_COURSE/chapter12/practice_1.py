try:
    with open('1.txt','r')as f:
        f.read()
    with open('2.txt','r')as f:
        f.read()
    with open('3.txt','r')as f:
        f.read()

except Exception as e:
    print(f"ths file is not present. Reason: {e}")

print("thanks for using this program")

