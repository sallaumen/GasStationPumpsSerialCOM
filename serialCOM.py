#!/usr/bin/python3
# -*- coding: utf-8 -*-
# at: 02/12/2018
import threading
import time
from inspect import getframeinfo, currentframe
import serial
from helper import exceptionLogger
from helper import syscall
import multiprocessing

class serialControler():
    def __init__(self, com):
        self.devComm = com #Ex: /dev/USB0

    def sendSerial(self, str_to_send):
        try:
            serialC = serial.Serial(self.devComm, baudrate=9600, timeout=2)
            serialC.write(str(str_to_send).encode())
            print("Enviado via serial: {0}".format(str_to_send))
            return 1
        except Exception as exc:
            print("Exception: {0}".format(exc))
            exceptionLogger("serialCOM.py", "sendSerial", getframeinfo(currentframe()).lineno, exc)


    def receiveSerial(self):
        try:
            serialC = serial.Serial(self.devComm, baudrate=9600, timeout=2)
            resposta = serialC.readline()
            resposta = resposta.decode().replace('\n', '')
            if resposta != "":
                print("Recebido via serial: {0}".format(resposta))
        except Exception as exc:
            print("Exception: {0}".format(exc))
            exceptionLogger("serialCOM.py", "sendSerial", getframeinfo(currentframe()).lineno, exc)
