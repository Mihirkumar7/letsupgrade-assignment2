# Write a program to check whether a string is a pangram or not.

# Pangram is a sentence or string which contains every letters of english alphabet.

def is_pangram(s):  # This function takes string as an argument.
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for ch in alphabets:
        if ch not in s.lower():
            return False
    return True


string = input('Enter the string to check : ')
if is_pangram(string):
    print('Yes it is pangram.')
else:
    print('No it is not pangram.')