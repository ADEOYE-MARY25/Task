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