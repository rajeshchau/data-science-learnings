a=[102,107,108,105,1034,1046]
b=["lucknow","rath","jhansi","banda","mohoda"]



#print(min(len(a),len(b)))

d={}

for i in range (min(len(a),len(b))):
    d.update({a[i]:b[i]})
    
print(d)