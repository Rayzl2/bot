# -*- coding: cp1251 -*-

file1 = open("log.txt", "r")

while True:
    # считываем строку
    line = file1.readline()
    # прерываем цикл, если строка пустая
    if not line:
        break
    # выводим строку
    print(line.strip())
    print(line.strip().split(":")[1])

# закрываем файл
file1.close