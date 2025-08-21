# # Task1: 
# # Create and display
# dish_1 = input("kindly enter a Nigerian dishes(one at a time:)")
# dish_2 = input("kindly enter a Nigerian dishes(one at a time:)")
# dish_3 = input("kindly enter a Nigerian dishes(one at a time:)") 
# dishes_tuple=(dish_1, dish_2, dish_3)
# print(f"\n'{dish_1} \n'{dish_2} \n'{dish_3} \n'")

# Task2:
# #Tuple and input
# friends_name= input("kindly enter your 5 best friends's name?:").split()
# friends_tuple=(friends_name)
# print(friends_tuple[::-1])


# Task3:
# Tuple operations
tuple1= input("kindly enter any state in Nigeria")
tuple2= input("kindly enter any state in Nigeria")
tuple3= input("kindly enter any state in Nigeria")
tuple4= input("kindly enter any state in Nigeri")
tuple5= input("kindly enter any state in Nigeri")
print(tuple2,tuple4)

# Task4:
# Tuple Unpacking
first_name = input("kindly enter your first name")
age = input("kindly enter your age")
favorite_color = input("kindly enter your favourite color")
home_town = input("kindly enter your home town")
profile_list= first_name, age, favorite_color, home_town
# Using escape sequence to align each piece of information
print(f"your personal information:\nName:{first_name}\nAge:{age}\nFavourite colour:{favorite_color}\nHome town:{home_town}")

# Task5:
# Modify Tuple Indirectly
item_lists= (
     (input("kindly enter  item in your shopping list one: ")),
     (input("kindly enter item in your shopping list two: ")),
     (input("kindly enter item in your shopping list third: ")) 
)
# List Converter
list_Converter= list(item_lists) 
list_Converter.append(input("kindly enter one extra item:")),
list_Converter.append(input("kindly enter last extra item:"))
my_item_list = tuple(list_Converter)
print("".join(my_item_list))



#6. # Attendance Tracker
# Write a python program that;
# stores the days of the week in a tuple.
days_of_the_week= tuple("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")
months_of_the_year= tuple("The months of the year are as follows:January, February, March, April, May, June, July, August, September, October, November, December")
student_name= input("kindly enter your name:")
Gender= input("kindly input your gender:") 
Course_Track= input("kindly input your course track")
current_month_num= input("kindly input current month number(1-12)")
Current_day_num= input("kindly input current day number(1-7)")
print(f"your name is:{student_name}, you are a:{Gender}, your course track is:{Course_Track}, your current month number is:{current_month_num} and your current day number is:{Current_day_num}")







#Task6:
# Attendance Tracker
# Write a python program that;



