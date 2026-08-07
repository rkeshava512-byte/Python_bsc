import time 
List_One=eval(input('Enter the list data type:'))
res1=[]
a=0 
while(a<len(List_One)):
    if(List_One[a] not in res1):
        res1.append(List_One[a])
    a+=1
print()
print("My list object with duplicate values:",List_One)
print()
print("After removing the duplicate objects:",res1)
print()
time.sleep(2)
print('End of an application')