#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Jan 2022
# List

from random import randint


def average(marks: list):
    # variable
    total = 0

    # process
    for mark in marks:
        total += mark

    # return average
    return int(total / len(marks))


def main():
    # main function for list

    # variables
    temp = ""
    marks = []

    # input
    while temp != "-1":
        temp = input("Mark (as %): ")
        marks.append(int(temp))
    marks.pop()

    # output/process/calling function
    print(f"Average is {average(marks)}%")

    # done
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
