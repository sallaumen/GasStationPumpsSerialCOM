#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Lucas C. Tavano
# at: 02/12/2018
import threading
import time
import json
from websocket import create_connection  # pip3 install socketIO-client-2
import ssl
from inspect import currentframe, getframeinfo
from datetime import datetime
from helper import exceptionLogger
from helper import syscall
from HWinfo import HWinfo


class WSHandler():
    def __init__(self):
        self.websocket_conn = 0
        self.websocket_broken = 0
        self.key = 0

    def WSConnCreator(self):
        """
        :return:1 if connection had success, 2 if it fails.
        """
        try:
            self.websocket_conn = create_connection("wss://18.228.62.35:81", sslopt={"cert_reqs": ssl.CERT_NONE})
            print("---> Socket_sync Conected")
            data_send = {"route": "register", "metaData": {"mac": HWinfo.detMAC().replace(':', '')}}
            self.websocket_conn.send(str(data_send))
            print("  Sended: {0}".format(data_send))
            raw_data = self.websocket_conn.recv()
            raw_data = json.loads(raw_data)
            self.websocket_conn.close()
            self.key = raw_data['metaData']['accesskey']
            print("  Key {0} Received".format(self.key))
            websocket_async = create_connection("wss://18.228.62.35:80", sslopt={"cert_reqs": ssl.CERT_NONE})
            print('--->Socket_async conected')
            data_send = {"route": "autenticar", "metaData": {"accesskey": self.key}}
            websocket_async.send(str(data_send))
            print("  Sended: {0}".format(data_send))
            return 1
        except Exception as exc:
            try:
                self.websocket_conn.close()
            except:
                pass
            print('\n--->Socket FAILED, exception:{0}'.format(exc))
            return 0

    def WSConnManager(self):
        """
        :return: none
        """
        while (1):
            try:
                if (self.websocket_broken == 1):
                    time.sleep(10)
                    con = self.WSConnCreator
                    if con == 1:
                        self.websocket_broken = 0
            except Exception as exc:
                print('websocket_broken, exception: {0}'.format(exc))
            time.sleep(60)

    def socketReceiver(self, serialCon):
        """
        :param serialCon:Object from serialControler class that is used to exchange data via serial
        :return: none
        """
        while 1:
            try:
                raw_data = self.websocket_conn.recv()
                print(" -->Received: {0}".format(raw_data))
                data = json.loads(raw_data)
                serialCon.sendSerial(data['assembly'])
                answer = ""
                while answer == "":
                    answer = serialCon.receiveSerial()
                answer = {'key':self.key, 'answer':answer}
                answer = json.dumps(answer)
                self.websocket_conn.send(str(answer))
                time.sleep(1)
            except Exception as exc:
                print("SocketReceiver error, exception: {0}".format(exc))
                time.sleep(10)


"""
    def internalHwDataStreamer():
        global websocket_async_broken
        while(1):
            try:
                ident = id_hotspot
                mac = HWinfo.detMAC()
                temp = HWinfo.detTemperature()
                status = HWinfo.detStatusHotspot()
                version = HWinfo.detVersion()
                cpu = HWinfo.detCPU()
                mem = HWinfo.detMemory()
                uptime = HWinfo.detUptime()
                OnlineNumber = HWinfo.detOnlineNumber()
                OnlineUsers = HWinfo.detOnlineUsers()
                serviceStatus_node = General_Info.serviceStatus()
                networking_node = Networking.networking()
                meta_data = {"id": ident, "mac": mac, "status": status, "version": version,"cpu": cpu, "memory": mem, "uptime": uptime, "temperature": temp, "online_number": OnlineNumber, "online_users": OnlineUsers, "servicesStatus": serviceStatus_node, "networkingStatus": networking_node}
                data = {"route": "internalHwDataStreamer", "metaData": meta_data}
                #data = str(data).replace("'",'"')
                websocket_async.send(str(data))
                print(" --->Sended: {0}".format(data))
                #server_response = socketReceiver(websocket_async)
                #print("\n\nRECEIVED: {0}".format(server_response))
                time.sleep(30)
            except Exception as exc:
                print("internalHwDataStreamer error, exception: {0}".format(exc))
                #exceptionLogger("flaskAPIBridge.py", "internalHwDataStreamer", getframeinfo(currentframe()).lineno, exc)
                websocket_async_broken = 1
                try:
                    websocket_async.close()
                except Exception as exc:
                    pass
                time.sleep(120)
"""
