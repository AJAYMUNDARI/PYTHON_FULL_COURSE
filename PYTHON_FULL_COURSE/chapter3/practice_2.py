#letter= ''' Dear <NAME>,
#           YOU ARTE SELECTED|
#           <DATE>


letter= ''' Dear <NAME>,
           YOU ARTE SELECTED|
           <DATE>'''
NAME=input("enter the name ")
DATE=input("enter the date ")
print(letter.replace('<NAME>',NAME).replace('<DATE>',DATE))