#create any variable convert from 
    # float -> int 
tax= 30.24
tax= int(tax)
taxtype=type(tax)
print(taxtype)
    #float -> str
taxStr= type(str(tax))
print(taxStr)

#Create a simple program to say weather is too cold or weather is perfect based on an inputed temperature 

temp= int(input("What is your environmnent's temprature? "))

if temp >= 20 :
    print("Your whether is hot")
else:
    print("Your whether is cold")
    