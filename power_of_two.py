#!/usr/bin/env python3

# Created By: Jessah
# Date: Nov 15, 2022
# This program ask the user for an integer and it will
# produce the power of the numbers before the input number


def main():
    # initialize the counter to 0
    counter = 0
    # get input from user
    user_string = input("Enter a whole number: ")

    try:  # catch decimals and strings
        user_int = int(user_string)
    except Exception:
        print("")
        print("{} is invalid, enter a whole number".format(user_string))
    else:
        if user_int >= 0:
            for counter in range(user_int + 1):  # for loop until user input
                power = counter**2
                print("{}^2 = {}".format(counter, power))
        else:
            print("{} is Invalid".format(user_int))
            print("Enter a whole number")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
