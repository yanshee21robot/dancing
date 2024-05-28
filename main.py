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
            1: 90,
            2: 90,
            3: 90,
            4: 90,
            5: 90,
            6: 90,        
        }, 300)

        #utils.Voice(method='tts', text='first position')

        time.sleep(2)
                
        utils.setRobotServo(RobotApi,
        {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
        }, 300)

        #utils.Voice(method='tts', text='second position')

        time.sleep(2)
                
        utils.setRobotServo(RobotApi,
        {
            1: 180,
            2: 180,
            3: 180,
            4: 180,
            5: 180,
            6: 180,
        }, 300)

        #utils.Voice(method='tts', text='third position')

        time.sleep(2)

        
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
