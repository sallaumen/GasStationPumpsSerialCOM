#!/usr/bin/python3
# -*- coding: utf-8 -*-
# at: 02/12/2018
import threading
import time
import serial       #pip3 install pyserial
import threading
from helper import exceptionLogger
from helper import syscall
from serialCOM import serialControler

def reader(serialObj):
    while 1:
        serialObj.receiveSerial()

def whileSender(serialObj):
    data = "start"
    while data != "end":
        data = input("Insira o dado que deseja enviar:\n"
                   " -->")
        serialObj.sendSerial(data)


if __name__ == "__main__":
    serialObj = serialControler("/dev/ttyUSB0")
    readThread = threading.Thread(target=reader, args=(serialObj,))
    readThread.start()
    whileSender(serialObj)