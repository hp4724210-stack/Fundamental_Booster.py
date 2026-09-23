

print("welcome to the interactive personal data collector!")
print()

name=input("enter your name")
age=int(input("enter your age"))
height=float(input("enter your height in meters"))
favnum=int(input("enter your fav num"))

print("thank you! here is the infromation we colleced")

print("name", name , "(type is:)" ,type(name), "memory address;",id(name),")")
print("age", age , "(type is:)" ,type(age), "memory address;",id(age),")")
print("height", height , "(type is:)" ,type(height), "memory address;",id(height),")")
print("fav num", favnum , "(type is:)" ,type(favnum), "memory address;",id(favnum),")")

print()

import datetime
current_year = datetime.datetime.now().year
birth_year = current_year - age 

print("your birth years is approximately", "year" ,"(based on your age)")

print("thank you for using the personal data collector good bye!")