import numpy as np


# Big Bad Sideeffect
def read_input():
    file1 = open("InputData.txt", "r")
    list_of_inputs = file1.readlines()
    file1.close()

    return list_of_inputs


# make input usable
def manipulate_input(input_list: list):
    for i in range(len(input_list)):
        input_list[i] = int(input_list[i][:-1])
    return input_list


def number_1():
    daily_data = manipulate_input(read_input())
    increased = 0
    for i in range(len(daily_data) - 1):
        if (daily_data[i] < daily_data[i + 1]):
            increased += 1
    print(increased)


def number_2():
    daily_data = manipulate_input(read_input())
    increased = 0
    for i in range(len(daily_data) - 3):
        if daily_data[i] + daily_data[i + 1] + daily_data[i + 2] < \
                daily_data[i + 1]+daily_data[i + 2]+daily_data[i + 3]:
            increased += 1
    print(increased)


# Probably not the most elegant solution (text me)
if __name__ == '__main__':
    number_1()
    number_2()
