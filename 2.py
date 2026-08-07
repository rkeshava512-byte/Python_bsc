import time 
List_One=eval(input('Enter the list data:'))
R=0 
x=0 
while(x<len(List_One)):
    R=R+List_One[x]
    x+=1
print("The result is:",R)
print()
time.sleep(2)
print("End of an application")


[12,76,13,24,19]