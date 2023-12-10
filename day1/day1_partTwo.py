with open("day1/day1.txt") as file:
        data = file.readlines()
number = ""
sum = 0
for line in data:
    line = line.replace("one", "one1one")
    line = line.replace("two", "two2two")
    line = line.replace("three", "three3three")
    line = line.replace("four", "four4four")
    line = line.replace("five", "five5five")
    line = line.replace("six", "six6six")
    line = line.replace("seven", "seven7seven")
    line = line.replace("eight", "eight8eight")
    line = line.replace("nine", "nine9nine")
    print(line)
    for char in line:
          if(char.isnumeric() and len(number) == 0):
                number += char
    for char in reversed(line):
          if(char.isnumeric() and len(number) == 1):
                number += char
    sum += int(number)
    number = ""
print(sum)