# Task1.
# File collector
fav_fruit= input("kindly enter your favourite five fruits:")
fruits= (fav_fruit)
print(f"this are your fruits:{fruits}")

# Task2:
# Unique Name Collector
# Names of people that attend a seminar
attendance_list = set()
attendance_list.add(input("kindly input your name for attendance purpose: "))
attendance_list.add(input("kindly input your name for attendance purpose: "))
attendance_list.add(input("kindly input your name for attendance purpose: "))
print("The names of people who attended the seminarare:", sorted(attendance_list))

#Task3:
# Simulate a football match ticket system
# store all seat numbers (1 to 50) in a set.
seat_numbers= set(range(1, 51))
seat_booked= int(input("kindly book a seat by entering a number"))
seat_numbers.remove(seat_booked)
print(seat_numbers)


#Task4:
# A unique voters Registration
voter_names= set()
voter_names.add(input("kindly input your name: ")).title()
voter_names.add(input("kindly input your name: ")).title()
voter_names.add(input("kindly input your name: ")).title()  #Duplicate, ignored automatically
print("voter_names:", voter_names)
# print(type(voter_names))
if name in voter_names:
    p