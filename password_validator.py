# import sys to be able to accept parameters from cmd
import sys


def password_validator():

    if len(sys.argv) > 1:
        password = sys.argv[1]
    else:
        password = ""   # pw input
    red = "\033[31m"    # setup error color
    green = "\033[32m"  # setup success color
    pw_len_flag = len(password) > 9     # min len of pw
    num_flag = False    # flag for num in pw
    char_flag = False   # flag for character in pw
    capital_letter_flag = False     # flag for capital letter in pw
    lowercase_flag = False      # flag for lower case letter in pw
    for char in str(password):
        if char.isnumeric():    # method checks if all the characters in the string are numeric
            num_flag = True
        else:
            if char.isalpha():      # check if all characters in the string are alphabets
                char_flag = True
                if char.isupper():      # method returns whether all characters in a string are uppercase or not
                    capital_letter_flag = True
                else:
                    lowercase_flag = True
    if pw_len_flag:
        print(green + "Length – Has Minimum of 10 characters.")
    else:
        print(red + "Password must have Minimum of 10 characters.")
    if char_flag and num_flag:
        print(green + "Contain both alphabet and number.")
    else:
        if not char_flag and not num_flag:
            print(red + "Password must contain both alphabet and number.")
        else:
            if not char_flag:
                print(red + "You should have at least 1 letter in password")
            if not num_flag:
                print(red + "You should have at least 1 num in password.")
    if capital_letter_flag and lowercase_flag:
        print(green + "Include both the lower and capital case letters.")
    else:
        if not capital_letter_flag and not lowercase_flag:
            print(red + "Password must contain both lower and capital case letters.")
        else:
            if not capital_letter_flag and lowercase_flag:
                print(red + "You should have at least 1 Capital case letter in password.")
            if not lowercase_flag and capital_letter_flag:
                print(red + "You should have at least 1 lower case letter in password.")
    if char_flag and char_flag and num_flag and lowercase_flag and capital_letter_flag:
        return 1
    else:
        return 0


def main():
    password_validator()


if __name__ == "__main__":
    main()
