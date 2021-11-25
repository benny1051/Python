import os
os.system('clear')

#This is a comment. 

fullName = "Benny Petersson"
age= 41

print("Hello World! and "+fullName)

fullName= "bob"

names= ["Lennart", "Måns", "Majlis"]
favPizza = {
	"Lennart" : "Pepperoni",
	"Måns" : "Mushroom",
	"Majlis" : "Cheese"
}

print(names+ names[0])# print the entire array and then print index 0
print(favPizza["Lennart"])# Vill be Pepperoni, Key: Value
