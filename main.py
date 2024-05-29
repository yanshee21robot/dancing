#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import utils
try:
    import commands
    import RobotApi
    api_check = True
except ImportError as e:
    print(e)
    print("Продолжить? (Y/N)")
    c = input("$> ")
    if c == 'N':
        quit()
    else:
        api_check = False


if api_check:
    # Инициализация SDK робота
    RobotApi.ubtRobotInitialize()

    # Подключение к SDK робота
    ret = RobotApi.ubtRobotConnect("SDK", "1", "127.0.0.1")
    if (0 != ret):
        print("Не удается подключиться к SDK робота")
        exit(1)

    isSetLed = False

def dancer():
    with open("test.txt", 'r', encoding='utf-8') as file:
        moves = file.readlines()
        for move in moves:
            dictionary = {}
            splitted_move = move.split(' ')
            for i in range(1, 18):
                try:
                    if not splitted_move[i-1] in ['_', '-']:
                        dictionary[i] = (splitted_move[i-1])
                    else:
                        pass
                except IndexError:
                    dictionary[i] = 0
            print(dictionary)

if __name__ == '__main__':

    servolist = {2: 90, 3: 90}
    utils.setRobotServo(RobotApi, servolist, 5000)
    
    print("Выполнение кода завершено!")

    if api_check:
        # Сброс сервоприводов робота
        RobotApi.ubtStartRobotAction("reset", 1)
        # Отключение от SDK робота
        RobotApi.ubtRobotDisconnect("SDK", "1", "127.0.0.1")
        # Деинициализация SDK робота
        RobotApi.ubtRobotDeinitialize()
