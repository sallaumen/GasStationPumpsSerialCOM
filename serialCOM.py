#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Lucas C. Tavano
# at: 02/12/2018
from inspect import getframeinfo, currentframe
import serial
import time
from helper import exceptionLogger


class serialControler:
    def __init__(self, com):
        self.devComm = com  # Ex: /dev/USB0
        while 1:
            try:
                self.serialC = serial.Serial(self.devComm, baudrate=9600, timeout=2)
                break
            except:
                print("Serial port {0} not found, trying to reconnect in 1 minute".format(self.devComm))
                time.sleep(60)

    def serialManager(self):
        """
        :return: none
        """
        while 1:
            try:
                self.serialC = serial.Serial(self.devComm, baudrate=9600, timeout=2)
                time.sleep(60)
            except:
                print("Serial port {0} not found, trying to reconnect in 1 minute".format(self.devComm))
                time.sleep(60)

    def sendSerial(self, str_to_send):
        try:
            self.serialC.write(str(str_to_send).encode())
            print("Sent via serial: {0}".format(str_to_send))
            return 1
        except Exception as exc:
            print("Exception: {0}".format(exc))
            exceptionLogger("serialCOM.py", "sendSerial", getframeinfo(currentframe()).lineno, exc)
            return 0

    def receiveSerial(self):
        try:
            answer = self.serialC.readline()
            answer = answer.decode().replace('\n', '')
            if answer != "":
                print("Received via serial: {0}".format(answer))
            return answer
        except Exception as exc:
            print("Exception: {0}".format(exc))
            exceptionLogger("serialCOM.py", "sendSerial", getframeinfo(currentframe()).lineno, exc)

    def reader(self):
        while 1:
            self.receiveSerial()

    def whileSender(self):
        data = "start"
        while data != "end":
            data = input("Insira o dado que deseja enviar:\n"
                         " -->")
            self.sendSerial(data)
