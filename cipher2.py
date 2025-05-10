import random
import string
# this program codes by rules of, if the number is atleast three it will reverse it and if its more it adds 3 random letters in front and in  the back.
# then it take the first letter of a word and places it t the end.
# If you want to decode reverse words with atleast 3 letters.
# remove first and last three letter and place the last letter in the first index.
a = str(input("Do you want to code or decode: "))

if(a!="code" and a!="decode"):
    raise ValueError("Enter code or decode")
elif(a=="code"):
    b = str(input("Enter what you want to code: "))
    words = b.split()
    coded_words = []
    
    for word in words:
        if len(word) <= 3:
            coded_words.append(word[::-1])
        else:
            new_word = word[1:] + word[0]
            random_letters = [random.choice(string.ascii_letters) for _ in range(6)]
            coded_word = (
                random_letters[0] +
                random_letters[1] +
                random_letters[2] +
                new_word +
                random_letters[3] +
                random_letters[4] +
                random_letters[5]
            )
            coded_words.append(coded_word)
            
        result = ' '.join(coded_words)
    print(f'The coded string is: "{result}"')
elif(a=="decode"):
    b = str(input("Enter what you want to code: "))
    words = b.split() # splits the words so they can be decoded
    coded_words = [] # Made a list to input mutliple words
    for word in words:
        if len(word) <= 3:
            coded_words.append(word[::-1]) 
        else:
            modified_word = word[3:-3]  # Remove the first 3 and last 3 letters
            modified_word = modified_word[-1] + modified_word[:-1]  # Move the last letter to the front
            coded_words.append(modified_word)
    print(" ".join(coded_words))
    
    