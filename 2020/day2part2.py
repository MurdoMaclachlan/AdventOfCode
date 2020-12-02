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
        nums.append(int("".join(num1)))
        nums.append(int("".join(num2)))
        listLine = line.split(":")
        rules = listLine[0]
        password = listLine[1]
        print(password)
        letterAmount = 0
        valid = False
        for i in range(len(list(password))):
            if i in [nums[0], nums[1]] and password[i] == rules[len(rules)-1] and valid == False:
                valid = True
            elif i in [nums[0], nums[1]] and password[i] == rules[len(rules)-1] and valid == True:
                valid = False
                print(i, password[i], rules[len(rules)-1], valid)
                break
            print(i, password[i], rules[len(rules)-1], valid)
        if valid:
            validPasswords.append(line)
            print(line + " VALID")
        else:
            print(line + " INVALID")
    print(len(validPasswords))
