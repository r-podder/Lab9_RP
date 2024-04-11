print("Menu")
print("-------------")
print("1. Encode")
print("2. Decode")
print("3. Quit")
option = input("Please enter an option: ")

if option == '1':
    password = input("Please enter your password to encode: ")
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    print("Your password has been encoded and stored!")

elif option == '2':
    encoded_password = input("Please enter your encoded password to decode: ")
    decoded_password = ""
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")

elif option == '3':
    exit()
