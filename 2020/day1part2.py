#!/usr/bin/env python3

# yes this code is shit why do you ask
with open("inputday1.txt", "r") as file:
    found = False
    content = file.read().splitlines()
    for line in content:
        if found == True:
            break
        secondValList = content.copy()
        secondValList.pop(secondValList.index(line))
        for secondVal in secondValList:
            if found == True:
                break
            thirdValList = secondValList.copy()
            thirdValList.pop(thirdValList.index(secondVal))
            for thirdVal in thirdValList:
                print(int(line) + int(secondVal) + int(thirdVal))
                if int(line) + int(secondVal) + int(thirdVal) == 2020:
                    found = True
                    print(f"The three numbers that make 2020 are {line}, {secondVal} and {thirdVal}, and their product is {int(line)*int(secondVal)*int(thirdVal)}.")
                    break
                else:
                    pass
