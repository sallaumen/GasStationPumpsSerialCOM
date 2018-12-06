#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Lucas C. Tavano
# at: 02/12/2018
import serial       #pip3 install pyserial
from inspect import currentframe, getframeinfo
import threading
from helper import exceptionLogger
from helper import syscall
from serialCOM import serialControler
from flaskAPIBridge import WSHandler

if __name__ == "__main__":
    try:
        #Cria Objeto da classe serial
        serialObj = serialControler("/dev/ttyUSB0")
        threadSerialManager = threading.Thread(target=serialObj.serialManager, args=())
        threadSerialManager.start()
        #readThread = threading.Thread(target=serialObj.reader, args=(serialObj,))
        #readThread.start()
        #serialObj.whileSender()

        #Estabelece conexao websocket
        ws = WSHandler()
        ws.WSConnCreator
        threadGerenciaWS = threading.Thread(target=ws.WSConnManager, args=())
        threadGerenciaWS.start()

        thread_internalHwDataStreamer = threading.Thread(target=ws.socketReceiver, args=serialObj)
        thread_internalHwDataStreamer.start()
    except Exception as exc:
        print("main error, exception: {0}".format(exc))
        exceptionLogger("flaskAPIBridge.py", "main", getframeinfo(currentframe()).lineno, exc)