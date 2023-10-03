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
# while True:
#     second_text = str(input("Please enter your text: "))
#     text_len = len(second_text)
#     if text_len == 0:
#         print("You should to enter something")
#         continue
#     else:
#         break
#
# while True:
#     second_char = str(input("Please enter your symbol what you want to find: "))
#     char_len = len(second_char)
#     if char_len == 0:
#         print("You should to enter something")
#         continue
#     elif char_len > 1:
#         print("You should to enter only one symbol")
#         continue
#     else:
#         break
#
# count_char = 0
# # for char in second_text:
# #     if char == second_char:
# #         count_char += 1
# #     else:
# #         continue
# # print(f"Count of '{second_char}' is : {count_char}")
#
# #якщо враховувати регістр
# lower_second_text = second_text.lower()
# lower_second_char = second_char.lower()
# for char in lower_second_text:
#     if char == lower_second_char:
#         count_char += 1
#     else:
#         continue
# print(f"Count of '{second_char}' is : {count_char}")

#Third task
# while True:
#     third_text = str(input("Please enter your text: "))
#     text_len = len(third_text)
#     if text_len == 0:
#         print("You should to enter something")
#         continue
#     else:
#         break
#
# while True:
#     third_word = str(input("Please enter word for changing: "))
#     word_len = len(third_word)
#     if word_len == 0:
#         print("You should to enter something")
#         continue
#     else:
#         break
#
# while True:
#     change_word = str(input("Please enter new word: "))
#     change_word_len = len(change_word)
#     if change_word_len == 0:
#         print("You should to enter something")
#         continue
#     else:
#         break
#
# if third_word in third_text:
#     print(third_text.replace(third_word, change_word))
# else:
#     print("Your word isn't in text")

#Fourth task
while True:
    text = str(input("Enter your text: "))
    text_len = len(text)
    if text_len == 0:
        print("You should to enter string")
        continue
    elif text_len < 10:
        print("You should to enter more then 10 characters")
        continue
    else:
        break

#1
print(f"Third character: '{text[2]}'")
#2
print(f"Penultimate character: '{text[len(text)-1]}'")
#3
print(f"the first five characters: '{text[:5]}'")
#4
print(f"the entire line except for the last two characters: '{text[:len(text)-2]}'")
#5
print(f"all characters with even indices: '{text[0:len(text):2]}'")
#6
print(f"all characters with odd indices : '{text[1:len(text):2]}'")
#7
print(f"all characters in reverse: '{text[len(text):0:-1]}'")
#8
print(f"all the characters of the string one by one in reverse: '{text[len(text):0:-2]}'")
#9
print(f"length of line: '{len(text)}'")