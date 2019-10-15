#!/usr/bin/env python3

# Created by: Joey Marcotte
# Created on: October 2019
# This program shows the greater number

import constants


def main():

    while True:
        # imput
        age = input("What is your age?:")

        # process
        try:
            age_as_number = int(age)
            if age_as_number > constants.MIN_AGE and \
               age_as_number < constants.MAX_AGE:
                # output
                print("You are of the right age to date my grandchild")
                break
            else:
                print("You are not of the right age to date my grandchild")
                break
        except(ValueError):
            print("That is not a valid age")
        finally:
            print("")


if __name__ == "__main__":
    main()
