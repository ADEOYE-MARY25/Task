# Task 2
# Comment the code below appropriately, and using doctring, explain what the code is doing.
# Federal Government Schorlaship Key Eligibility Requierments:
# The Applicant must be a citizen of Nigeria.


name = input("Enter your name: ") 
# You are to input your name 
#ouput: Tope

age = int(input("Enter your age: "))
# You are to input your age in the space above
# output Age: 56

score = int(input("Enter your test score: "))
# You are to input your score in the space above
# output Scorce: 54

eligibility = (age < 18)   and (score > 70)
# This means that age is less than 18   and score is greater than 70
# output is False

citizenship = input("kindly input your nationality: ").title()

Enrollment = input(" kindly indicate if you are a full-time undergraduate student in a recognized Nigerian university")
other_Scholarship= input(" Are you currently receiving any schorlaship from an entity in the Oil and Gas industry:")
Academic_Qualification = input(" kindly input five distinctions (As and Bs) in relevant subjects either WAEC/WASSCE(May/June) exams, including English and Mathematics")

print(f"candidate: {name}\nAge: {age}\nscore: {score}\nEligible: {eligibility}")
# f fuction combine the sentence together and \n allows new line for each word before it.
# output 
candidate: 67
Age: 56
score: 54
Eligible: False