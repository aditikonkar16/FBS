li=[40,10,40,30,20]
li.append(50)
li.clear()

li=[40,10,40,30,20,[90,100]]
li2=li.copy()
li[5][0]=70
print(li)
print(li2)

print(li.count(40))
li.extend([70,80])
print(li.index(30)) #shows the index vaule 
li.insert(1,90)
li.pop(4) # removes the value of the index we have mentioned
li.remove(50)
li.reverse() #gives in reverse order
li.sort() # sorts the list
li.sort(revrese=True) #sorts the list in descending order
print(li)
