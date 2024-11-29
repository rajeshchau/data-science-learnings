d={}

data = 3

while data>0:
    k=int(input("enter the key:"))
    da=input("enter the data:")
    d.update({k:da})
    data-=1
    
print(d)