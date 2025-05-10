import random
import string

a = str(input("Do you want to code or decode: "))

if(a!="code" and a!="decode"):
    raise ValueError("Enter Code or Decode")
elif(a=="code"):
    b = str(input("Enter what you want to code: "))
    words = b.split()

    for word in words:  # Loop through each word in the list
        for letter in word:  # Loop through each character in the word
            asc = ord(letter)  # Get the ASCII value of the character
            new_asc = asc + 3  # Shift ASCII value by 3
            new_letter = chr(new_asc)  # Convert shifted value back to character
            print(new_letter, end="")  # Print the encoded character
        print(" ", end="")  # Add space after each encoded word
                                                                            
elif(a=="decode"):
    b = str(input("Enter what you want to code: "))
    words = b.split()
    for word in words:  # Loop through each word in the list
        for letter in word:  # Loop through each character in the word
            asc = ord(letter)  # Get the ASCII value of the character
            new_asc = asc - 3  # Shift ASCII value by 3
            new_letter = chr(new_asc)  # Convert shifted value back to character
            print(new_letter, end="")  # Print the encoded character
        print(" ", end="")  # Add space after each encoded word
    
