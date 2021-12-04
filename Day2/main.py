import re


# Big Bad Sideeffect
def read_input():
    file1 = open("InputData.txt", "r")
    list_of_inputs = file1.readlines()
    file1.close()

    return list_of_inputs


# make input usable
def manipulate_input(input_list: list):
    for i in range(len(input_list)):
        input_list[i] = input_list[i][:-1]
    return input_list

def number_1():
    depth = 0
    position = 0
    commands = manipulate_input(read_input())
    for x in commands:
        if re.search('^f.', x):
            position += int(re.findall('\d+$', x)[0])
        if re.search('^u.', x):
            depth -= int(re.findall('\d+$', x)[0])
        if re.search('^d.', x):
            depth += int(re.findall('\d+$', x)[0])
    print(depth * position)

def number_2():
    depth = 0
    position = 0
    aim = 0
    commands = manipulate_input(read_input())
    for x in commands:
        amount = int(re.findall('\d+$', x)[0])
        if re.search('^f.', x):
            position += amount
            depth += amount * aim
        if re.search('^u.', x):
            aim -= amount
        if re.search('^d.', x):
            aim += amount
    print(depth * position)


if __name__ == '__main__':
    number_1()
    number_2()