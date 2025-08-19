# Task 5
# Contact Quick Lookup
names = ("Tope", "Taiwo", "Bukayo")
phone_num = (+23470693060, +23450918456, +23450901278)
contacr_dict = {name: phone for name, phone in zip(names, phone_num)}
lookup_name = input ("kindly enter the missing name: ")
if lookup_name in names:
    print(f"the corresponding phone number for {lookup_name} is {contacr_dict}")
else:
    print("contact not found")
    # print (contact_dict)

