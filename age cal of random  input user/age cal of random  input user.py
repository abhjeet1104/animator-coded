# calcualte the age of the user

name = input("Name: ") 
place = input("place: ")
year_of_birth = input("year_of_birth: ") 
current_year = input("current year: ")
age = int(current_year) - int(year_of_birth)

print(f"""
My name is: {name}
I live at: {place}
{name} is of age: {age}
""")
