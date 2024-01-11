#hindi to english trans
word={"pani":"water",
      "kursi":"chair",
      "kalam":"pen"}
hindi=input("enter the word ")
if(word.get(hindi)==None):
    print("value not found")
else:
    print("value is: ",word.get(hindi)) 