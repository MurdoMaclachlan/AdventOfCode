#!/usr/bin/env python3

with open("inputday1.txt", "r") as file:
    content = file.read().splitlines()
    for line in content:
        compareList = content
        compareList.pop(compareList.index(line))
        for value in compareList:
            if int(line) + int(value) == 2020:
                print(f"The two numbers that make 2020 are {line} and {value}, and their product is {int(line)*int(value)}.")
                break
            else:
                pass
