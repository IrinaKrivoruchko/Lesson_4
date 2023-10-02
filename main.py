# #First task
# while True:
#     first_text = str(input("Please enter your text: "))
#     text_len = len(first_text)
#     if text_len == 0:
#         print("You should to enter something")
#         continue
#     else:
#         break
#
# str_count = 0
# int_count = 0
#
# for char in first_text:
#     if char.isdigit():
#         int_count +=1
#     else:
#         str_count +=1
# print(f"Count of integer in your text: {int_count}")
# print(f"Count of string in your text: {str_count}")

#Second task
while True:
    second_text = str(input("Please enter your text: "))
    text_len = len(second_text)
    if text_len == 0:
        print("You should to enter something")
        continue
    else:
        break

while True:
    second_char = str(input("Please enter your symbol what you want to find: "))
    char_len = len(second_char)
    if char_len == 0:
        print("You should to enter something")
        continue
    elif char_len > 1:
        print("You should to enter only one symbol")
        continue
    else:
        break

count_char = 0
# for char in second_text:
#     if char == second_char:
#         count_char += 1
#     else:
#         continue
# print(f"Count of '{second_char}' is : {count_char}")

#якщо враховувати регістр
lower_second_text = second_text.lower()
lower_second_char = second_char.lower()
for char in lower_second_text:
    if char == lower_second_char:
        count_char += 1
    else:
        continue
print(f"Count of '{second_char}' is : {count_char}")

