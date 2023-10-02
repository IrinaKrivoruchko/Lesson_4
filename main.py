#First task
while True:
    first_text = str(input("Please enter your text: "))
    text_len = len(first_text)
    if text_len == 0:
        print("You should to enter something")
        continue
    else:
        break

str_count = 0
int_count = 0

for char in first_text:
    if char.isdigit():
        int_count +=1
    else:
        str_count +=1
print(f"Count of integer in your text: {int_count}")
print(f"Count of string in your text: {str_count}")

