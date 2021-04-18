# ask user for name

name = input('what is your name?: ')


#ask user for age

age = input('enter your age?: ')

#ask user for city

city = input('what city do you live in?: ')

#ask user what they enjoy

enjoy = input('what do enjoy doing?: ')

#create output

string = 'your name is {} and you are {} years old. you live in {} and you enjoy {}'
output = string.format(name,age,city,enjoy)

#print output to screen

print(output)
