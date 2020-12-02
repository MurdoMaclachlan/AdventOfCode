#!/usr/bin/env python3

with open("inputday2.txt", "r") as file:
    content = file.read().splitlines()
    validPasswords = []
    for line in content:
        num1, num2, nums = [], [], []
        first = True
        for char in list(line):
            if char.isnumeric() and first:
                num1.append(char)
            elif char.isnumeric() and not first:
                num2.append(char)
            elif char == "-":
                first = False
        nums.append("".join(num1))
        nums.append("".join(num2))
        listLine = line.split(":")
        rules = listLine[0]
        letterAmount = 0
        for char in list(listLine[1]):
            if char == list(rules)[len(list(rules))-1]:
                letterAmount += 1
        if letterAmount < int(nums[0]) or letterAmount > int(nums[1]):
            print(line + " INVALID")
        else:
            validPasswords.append(line)
            print(line + " VALID")
    print(len(validPasswords))
