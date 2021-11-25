#Benny Petersson, Learning python
import os
os.system('clear')
#This is a comment. 
#git add .
#git commit - am "comment"
#git push

fullName = "Benny Petersson"
age= 41

names= ["Lennart", "Måns", "Majlis"] #Array
favPizza = { # key, value
	"Lennart" : "Pepperoni",
	"Måns" : "Mushroom",
	"Majlis" : "Cheese"
}

print("Hello World! and "+ fullName)
print(names[0])# print index 0
print(favPizza["Lennart"])# Vill be Pepperoni, Key: Value

greetings = "My boss yelled \"get back to work\"" # do a quote with escape character
name= "John"
greetings = "hello, my name is " + name # Adding strings together
print(greetings)

print(greetings.upper()) #When using string method make the .() after. 
print(len(greetings)) # Print the length of the String. 
print(greetings[2:5]) # Should return llo of the string Hello, #making array out of String
print(greetings.split(" ")[1:4]) # Splits the string into subparts for array
num=10
print(float(num)) #print en int, men gör om den till float i metoden.
print(5**2) #exponential funktion
print(11%2) # modulus, return 1. If modulus is 0 the number is dividable. 
print(str(num)+" hej ") #convert the int to string so you can put strings together 