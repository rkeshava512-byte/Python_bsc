d1={'AP':'Amaravati',"AP":'GUNTUR','MH':'Munbai',2:4,8:64,2:16}
print(d1)
print(type(d1))
print(d1.keys())
print(d1.values())

#Dictionary Methods
#1.get()
print(d1.get('AP'))

#2.popintem()
print(d1.popitem())
print(d1)

#setdefault
d2="name","keshav"
d1.setdefault(d2)
print(d1)