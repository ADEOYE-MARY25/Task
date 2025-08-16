# Task4:
# Tuple Unpacking
first_name = input("kindly enter your first name")
age = input("kindly enter your age")
favorite_color = input("kindly enter your favourite color")
home_town = input("kindly enter your home town")
profile_list= first_name, age, favorite_color, home_town
# Using escape sequence to align each piece of information
print(f"your personal information:\nName:{first_name}\nAge:{age}\nFavourite colour:{favorite_color}\nHome town:{home_town}")
