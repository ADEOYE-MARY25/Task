# Task1:
# Your Favourite Life Quote
quote = input("kindly input your favourite quote: ")
quote = quote.title()
print(f'\"{quote}\"')

#Task2
#Shopping list Manager
empty = []
items = input(" kindly enter 3 shopping items one by one with commas in between ")
items()
empty = items.copy()
print(empty)

#Task3
# Word Countter
sentence= input ("kindly enter a senterce: ")
sentence_list = list(sentence.split())  #this convert the inputed sentence to list
print(sentence_list)


# Task4
# Name Organizer
# names = []
#for m in range(2):
list_of_names =input("kindly input 5 names seperated by space: ")
# create case converter
create_case_converter= list_of_names.lower()
#sort the list
splitter = create_case_converter.split()
splitter.sort()
print(*splitter, sep="\n")



# Task5:
#  Student Score Tracker
#Create a student name that is empty list
#list_name =[]
#list_score =[]
student_name =[]
student_score= []
name_1= input("kindly input first name of student")
name_2= input("kindly input student second name")
name_3= input("kindly input student second name")

score_1= int(input("enter score for sudent one: "))
score_2= int(input("enterscore for student one:"))
score_3= int(input("enter score for student one:"))

# Append student name
student_name.append(name_1)
student_name.append(name_2)
student_name.append(name_3)
print(f"\nName:{student_name}\nscore:{student_score}")

# Task 6
# Word Analyzer
word = input("pleace enter a word: ")
print(word)
print(word,len(word))
print(word.isupper())
print(word.islower())
print(word.title())

# Task 7
#list multiplication
#city name list
cities_name =["Ogun","Oyo","Osun", "Ibadan", "Jos"]
# replacement of the thrid name
city_name_reqt= str(input("Input a city name of your choice: "))
# remove osun
cities_name.remove("Osun")
# insert a new city name
cities_name.insert(2, city_name_reqt)
# remove last city
cities_name.remove("Jos")
# insert a new city at the begining of the cities
cities_name.insert(9,"Kano")
print(cities_name)