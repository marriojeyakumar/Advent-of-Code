with open("day1/day1.txt") as file:
        data = file.readlines()
number = ""
sum = 0
for line in data:
    print(line)
    for char in line:
          if(char.isnumeric() and len(number) == 0):
                number += char
    for char in reversed(line):
          if(char.isnumeric() and len(number) == 1):
                number += char
    print(number)
    sum += int(number)
    number = ""
print(sum)