#!/usr/bin/python
# -*- coding: utf-8 -*-
def SetMotion(RobotApi, command, direction, time, speed):
    """
    Управляет движением робота, используя заданные команды и параметры.

    Аргументы:
    RobotApi: API для управления роботом.
    command: Команда движения робота (например, "crouch" - присесть, "raise" - поднять руку, "walk" - ходить).
    direction: Направление движения или часть тела (например, "left" - лево, "front" - вперед, "back" - назад).
    time: Продолжительность выполнения команды в секундах.
    speed: Скорость выполнения команды.

    Примеры использования:
    # Присесть
    SetMotion(RobotApi, "crouch", "", 2, 1)
    
    # Поднять левую руку
    SetMotion(RobotApi, "raise", "left", 3, 1)
    
    # Повернуть голову влево
    SetMotion(RobotApi, "head", "left", 3, 1)
    
    # Идти вперед
    SetMotion(RobotApi, "walk", "front", 1, 2)
    
    # Идти назад
    SetMotion(RobotApi, "walk", "back", 3, 10)
    """
    RobotApi.ubtSetRobotMotion(command, direction, time, speed)


def StartAction(RobotApi, action, repetitions):
    """
    Начинает выполнение заданного действия робота.

    Аргументы:
    RobotApi: API для управления роботом.
    action: Действие, которое должен выполнить робот (например, "knee left" - наклониться налево, "Left hits forward" - ударить вперед левой рукой).
    repetitions: Количество повторений действия.

    Примеры использования:
    # Наклониться налево
    StartAction(RobotApi, "knee left", 1)
    
    # Ударить вперед левой рукой
    StartAction(RobotApi, "Left hits forward", 1)
    """
    RobotApi.ubtStartRobotAction(action, repetitions)


def setRobotLED(RobotApi, what='button', color="green", type='blink'):
    """
    Устанавливает цвет и режим работы светодиода на роботе.

    Аргументы:
    RobotApi: API для управления роботом.

    Пример использования:
    SetRobotLED(RobotApi, "button", "red", "breath")
    """
    # Устанавливаем светодиод на кнопке робота в красный цвет и режим мигания
    RobotApi.ubtSetRobotLED(what, color, type)


def Voice(RobotApi, method='play', **kwargs):
    """
    Управляет голосовыми функциями робота: проигрывание музыки или преобразование текста в речь.

    Аргументы:
    RobotApi: API для управления роботом.
    method: Метод голосового управления ('play' для проигрывания музыки, любое другое значение для преобразования текста в речь).
    kwargs: Дополнительные аргументы. Для метода 'play' требуется аргумент 'path' (путь к музыкальному файлу). Для преобразования текста в речь требуется аргумент 'text'.

    Пример использования:
    Voice(RobotApi, method='play', path='/path/to/music.mp3')
    Voice(RobotApi, method='tts', text='Hello, world!')
    """
    if method == 'play':
        # Проигрываем музыку, используя указанный путь к файлу
        RobotApi.ubtPlayMusic('play', kwargs['path'])
    else:
        # Преобразуем текст в речь, используя указанный текст
        RobotApi.ubtVoiceTTS(0, kwargs['text'])


def setRobotServo(RobotApi, servolist, time):
    """
    Устанавливает углы поворота для сервомоторов робота.

    Аргументы:
    RobotApi: API для управления роботом.
    servolist: Словарь, где ключи - это ID сервомоторов, а значения - углы поворота.
    time: Время в миллисекундах для выполнения поворота.

    Возвращает:
    int: Результат выполнения команды установки углов сервомоторов.

    Пример использования:
    servolist = {1: 90, 2: 45, 3: 135}
    setRobotServo(RobotApi, servolist, 1000)
    """
    
    # Создание экземпляра структуры данных для хранения информации о сервомоторах
    servoinfo = RobotApi.UBTEDU_ROBOTSERVO_T()
    
    # Установка углов для каждого сервомотора на основе предоставленного словаря
    for servo_id, servo_angle in servolist.items():
        print("servoid = %d, servoangle = %d\n" % (servo_id, servo_angle))
        if servo_id == 1:
            servoinfo.SERVO1_ANGLE = servo_angle
        elif servo_id == 2:
            servoinfo.SERVO2_ANGLE = servo_angle
        elif servo_id == 3:
            servoinfo.SERVO3_ANGLE = servo_angle
        elif servo_id == 4:
            servoinfo.SERVO4_ANGLE = servo_angle
        elif servo_id == 5:
            servoinfo.SERVO5_ANGLE = servo_angle
        elif servo_id == 6:
            servoinfo.SERVO6_ANGLE = servo_angle
        elif servo_id == 7:
            servoinfo.SERVO7_ANGLE = servo_angle
        elif servo_id == 8:
            servoinfo.SERVO8_ANGLE = servo_angle
        elif servo_id == 9:
            servoinfo.SERVO9_ANGLE = servo_angle
        elif servo_id == 10:
            servoinfo.SERVO10_ANGLE = servo_angle
        elif servo_id == 11:
            servoinfo.SERVO11_ANGLE = servo_angle
        elif servo_id == 12:
            servoinfo.SERVO12_ANGLE = servo_angle
        elif servo_id == 13:
            servoinfo.SERVO13_ANGLE = servo_angle
        elif servo_id == 14:
            servoinfo.SERVO14_ANGLE = servo_angle
        elif servo_id == 15:
            servoinfo.SERVO15_ANGLE = servo_angle
        elif servo_id == 16:
            servoinfo.SERVO16_ANGLE = servo_angle
        elif servo_id == 17:
            servoinfo.SERVO17_ANGLE = servo_angle

    # Установка углов сервомоторов с учетом времени выполнения
    ret = RobotApi.ubtSetRobotServo(servoinfo, time / 20)
    
    return ret
