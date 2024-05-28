#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import commands
import RobotApi
import utils

# Инициализация SDK робота
RobotApi.ubtRobotInitialize()

# Подключение к SDK робота
ret = RobotApi.ubtRobotConnect("SDK", "1", "127.0.0.1")
if (0 != ret):
    print("Не удается подключиться к SDK робота")
    exit(1)

isSetLed = False

if __name__ == '__main__':
    try:
        
        utils.setRobotServo(RobotApi,
        {
            1: 30,
            2: 0,
            3: 0,
        }, 300)

        #if (RobotApi.ubtVisionDetect("face", "0", 20) == 0):
        #    pass

        print("Выполнение кода завершено!")
    except:
        print("Ошибка выполнения")

    # Сброс сервоприводов робота
    RobotApi.ubtStartRobotAction("reset", 1)
    # Отключение от SDK робота
    RobotApi.ubtRobotDisconnect("SDK", "1", "127.0.0.1")
    # Деинициализация SDK робота
    RobotApi.ubtRobotDeinitialize()
