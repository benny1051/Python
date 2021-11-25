#Benny Petersson, Learning python
import os
os.system('clear')

#This is a comment. 

fullName = "Benny Petersson"
age= 41

print("Hello World! and "+fullName)

fullName= "bob"

names= ["Lennart", "Måns", "Majlis"] #Array
favPizza = { # key, value
	"Lennart" : "Pepperoni",
	"Måns" : "Mushroom",
	"Majlis" : "Cheese"
}

print(names[0])# print index 0
print(favPizza["Lennart"])# Vill be Pepperoni, Key: Value
