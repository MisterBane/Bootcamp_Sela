import sys
from colorama import init


def password_validator():
    """
    function to validate a password with certain requirements and provides an output :

    Password Requirements:
        (1) Length – minimum of 10 characters.
        (2) Contain both alphabet and numerical.
        (3) Include both lower and upper case letters.

    Function Exceptions:

    (1) Color output Green or Red.
         (1.1) Green = passed the validation.
             (1.2) Red = not passed the validation.

    (2) Return exit code 0 or 1.
         (2.1) 0 = passed the validation.
             (2.2) 1 = not passed the validation.

    (3) If a validation failed provide a message explaining why.

    How to use password_validator.py

        1) Run with CMD and send a "password":
            Commend line example -> : (python ./password_validator.py "Password1!")
            function Get password as "Password1!" (wright your "password" to check)

        2) Run with CMD and ask to read "password" from a file with a file path:
            Commend line example -> : (python ./password_validator.py -f "/mypath/password.txt")

        :return: sys.exit(code) 0 = valid ,1 = invalid.
        """
    
    init(autoreset=True)
    red = "\033[31m"
    green = "\033[32m"
    file_path = ""
    if len(sys.argv) > 1:
        if len(sys.argv) == 3:
            password = sys.argv[1]
            if password == "-f":
                try:
                    file_path = sys.argv[2]
                except IndexError:
                    print(red + "Invalid Password.")
                    print("function -f sent with out a file Path")
                    exit(1)
                try:
                    with open(file_path, "r") as file_path_password:
                        password = file_path_password.read()
                except OSError:
                    print(red + "Invalid Password.")
                    print("Invalid file Path : No such file or directory, Please check if file exist and path is correct")
                    exit(1)
            else:
                print(red + "Invalid Password.")
                print(f"Function {password} Unrecognized")
                exit(1)
        else:
            if len(sys.argv) == 2 :
                password = sys.argv[1]
            else:
                print(red + "Invalid Password.")
                print("Got more then 1 arguments - can't run the validator")
                exit(1)
    else:
        password = ""
    pw_len_flag = len(password) > 9
    char_flag = False
    num_flag = False
    lowercase_flag = False
    capital_letter_flag = False
    for char in str(password):
        if char.isnumeric():
            num_flag = True
        else:
            if char.isalpha():
                char_flag = True
                if char.isupper():
                    capital_letter_flag = True
                else:
                    lowercase_flag = True
    if pw_len_flag and num_flag and lowercase_flag and capital_letter_flag:
        print(green + "Valid Password")
        return exit(0)
    else:
        print(red + "Invalid Password.")
        counter_msg = 1
    if not pw_len_flag:
        print("("+str(counter_msg)+")", "Password too short - Minimum of 10 characters")
        counter_msg += 1
    if not num_flag or not char_flag:
        print("("+str(counter_msg)+")", "Password requires alphabet and numerical chars")
        counter_msg += 1
    if not capital_letter_flag or not lowercase_flag:
        print("("+str(counter_msg)+")", "Password requires upper and lower case chars")
    return exit(1)


def main():
    password_validator()


if __name__ == "__main__":
    main()
