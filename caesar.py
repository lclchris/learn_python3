def caesar_encrypt(text):
    result = ""
    # Go through each character of the text in this for loop
    for i in range(len(text)):
        # Obtain the ASCII value using ord
        char_position = ord(text[i])
        if(chr(char_position).isupper() == True):
            char_position = char_position - 65
            new_char_position = char_position + 3
            new_char_position = new_char_position % 26
            new_char_position = new_char_position + 65
            result = result + chr(new_char_position)
#            print(result)
        elif(chr(char_position).isupper() == False and (char_position > 64 and char_position < 91) or (char_position > 96 and char_position < 123)):
            # Substract 97 to have a character from 1 to 26
            char_position = char_position - 97
            # Add 3 to the position, as caesar does
            new_char_position = char_position + 3
            # Make sure that the position does not surpass 26 (we wrap around)
            new_char_position = new_char_position % 26
            # Convert back to ASCII values
            new_char_position = new_char_position + 97
            # Convert ASCII value to character and concatenate it to final result
            result = result + chr(new_char_position)
#            print(result)
        else:
            result = result + chr(char_position)
    return result
def caesar_decrypt(cipher_text):
    result = ""
    # Go through each character of the text in this for loop
    for i in range(len(cipher_text)):
        # Obtain the ASCII value using ord
        char_position = ord(cipher_text[i])
        if(chr(char_position).isupper() == True):
            char_position = char_position - 65
            new_char_position = char_position - 3
            new_char_position = new_char_position % 26
            new_char_position = new_char_position + 65
            result = result + chr(new_char_position)
#            print(result)
        elif(chr(char_position).isupper() == False and (char_position > 64 and char_position < 91) or (char_position > 96 and char_position < 123)):
            # Substract 97 to have a character from 1 to 26
            char_position = char_position - 97
            # Substract 3 to the position, to get back original position
            new_char_position = char_position - 3
            # Make sure that the position does not surpass 26 (we wrap around)
            new_char_position = new_char_position % 26
            # Convert back to ASCII values
            new_char_position = new_char_position + 97
            # Convert ASCII value to character and concatenate it to final result
            result = result + chr(new_char_position)
 #           print(result)
        else:
            result = result + chr(char_position)
    return result
print("\n" + "="*10 + " EXAMPLE " + "="*10)
text = "picocTFa=@;'0-z"
print(f"Plain Text: {text}")
cipher_text = caesar_encrypt(text)
print(f"Encrypted: {cipher_text}")
print(f"Decrypted: {caesar_decrypt(cipher_text)}")
print("="*29)
print("**note: Number and Special character wouldn't be encrypted/decrypted!\n")
print("="*7 + " Your Option: " + "="*7)
print("1. Encrypt")
print("2. Decrypt\n")
choosen_option = input()
print("")

if choosen_option == "1":
    print("Input your text to Encrypt: ")
    user_text = input()
    print(f"\nEncrypted: {caesar_encrypt(user_text)}")
elif choosen_option == "2":
    print("Input your text to Decrypt: ")
    user_text = input()
    print(f"\nDecrypted: {caesar_decrypt(user_text)}")
else:
    print("Please choose the number within option!")
