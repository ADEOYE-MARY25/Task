
#Task3:
# Simulate a football match ticket system
# store all seat numbers (1 to 50) in a set.
seat_numbers= set(range(1, 51))
seat_booked= int(input("kindly book a seat by entering a number"))
seat_numbers.remove(seat_booked)
print(seat_numbers)