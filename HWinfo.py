#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Lucas C. Tavano
# at: 18/06/2018
from inspect import currentframe, getframeinfo
from helper import exceptionLogger
from helper import syscall


class HWinfo():
    def __init__(self):
        pass

    @staticmethod
    def detMAC():
        # Pegando mac
        mac = "Error"
        try:
            mac = syscall("cat /sys/class/net/eth0/address")[0].replace('\n', '')
            return str(mac)

        except Exception as exc:
            mac = "None"
            print("Erro na coleta do mac - Exception = %s" % (str(exc)))
            exceptionLogger("HWinfo.py", "mac", getframeinfo(currentframe()).lineno, exc)
            return mac

    @staticmethod
    def detTemperature():
        # Pegando temperatura
        temperature = "Error"
        try:
            temperature = syscall("cat /sys/devices/virtual/thermal/thermal_zone0/temp")[0].replace('\n', '')
            if syscall("""uname -a | awk '{print $3}'""")[0] == '4.14.18-sunxi':
                temperature = int(temperature) / 1000
            else:
                temperature = int(temperature)
            return str(temperature)
        except Exception as exc:
            temperature = "Error"
            print("Erro na coleta da temperatura - Exception = %s" % (str(exc)))
            exceptionLogger("HWinfo.py", "detTemperature", getframeinfo(currentframe()).lineno, exc)
            return "-1"

    @staticmethod
    def detCPU():
        # Pegando CPU%
        cpu = "Error"
        try:
            cpu = syscall("grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage \"%\"}'")[
                0].replace('\n', '')
            return str(cpu)
        except Exception as exc:
            cpu = "Error"
            print("Erro na coleta da cpu - Exception = %s" % (str(exc)))
            exceptionLogger("HWinfo.py", "detCPU", getframeinfo(currentframe()).lineno, exc)
            return "-1"

    @staticmethod
    def detUptime():
        # Pegando uptime
        uptime = "Error"
        try:
            uptime = syscall("uptime -p")[0].replace('\n', '')
            return str(uptime)
        except Exception as exc:
            uptime = "Error"
            print("Erro na coleta da uptime - Exception = %s" % (str(exc)))
            exceptionLogger("HWinfo.py", "uptime", getframeinfo(currentframe()).lineno, exc)
            return "-1"

    @staticmethod
    def detMemory():
        # Pegando memory
        mem = "Error"
        try:
            mem = syscall("free | grep Mem | awk '{usage=($3/$2)*100} END {print usage \"%\"}'")[0].replace('\n', '')
            return str(mem)
        except Exception as exc:
            mem = "Error"
            print("Erro na coleta da memory - Exception = %s" % (str(exc)))
            exceptionLogger("HWinfo.py", "mem", getframeinfo(currentframe()).lineno, exc)
            return "-1"

    @staticmethod
    def detInterface():
        # Pegando interface wlan
        interface = "Error"
        try:
            interface = syscall("""iw dev | awk '$1=="Interface"{print $2}'""")[0].replace('\n', '')
            return str(interface)
        except Exception as exc:
            interface = "None"
            print("Erro na coleta da interface - Exception = %s" % (str(exc)))
            exceptionLogger("HWinfo.py", "interface", getframeinfo(currentframe()).lineno, exc)
            return interface

    @staticmethod
    def detOnlineNumber():
        # Pegando online Number
        online = "Error"
        try:
            online_file = open('/root/info/online', 'r')
            online = online_file.read()
            online_file.close()
            if online == "\n" or online == "":
                online = 0
            online = online.replace("\n", "")
            return str(online)
        except Exception as exc:
            online = "Error"
            print("Erro na coleta de onlines - Exception = %s" % (str(exc)))
            exceptionLogger("HWinfo.py", "OnlineNumber", getframeinfo(currentframe()).lineno, exc)
            return "0"

    @staticmethod
    def detOnlineUsers():
        # Pegando online users
        users = "Error"
        try:
            users_file = open('/root/info/users', 'r')
            users = users_file.read()
            users_file.close()
            users = str(users).replace('[', '').replace(']', '').replace(' ', '').replace("'", '').split(',').replace(
                "\n", "")
            return (users)
        except Exception as exc:
            users = "Error"
            return "[]"

    @staticmethod
    def detStatusHotspot():
        # Pegando status
        status = "Error"
        try:
            status_file = open('/root/info/status', 'r')
            status = status_file.read()
            status_file.close()
            if status == "\n" or status == "":
                status = 0
            status = status.replace("\n", "")
            return str(status)
        except Exception as exc:
            status = "Error"
            print("Erro na coleta de status - Exception = %s" % (str(exc)))
            exceptionLogger("HWinfo.py", "detStatusHotspot", getframeinfo(currentframe()).lineno, exc)
            return "0"

    @staticmethod
    def detVersion():
        # Pegando version
        version = "Error"
        try:
            version_file = open('/root/info/version', 'r')
            version = version_file.read()
            version_file.close()
            version = version.replace("\n", "")
            return str(version)
        except Exception as exc:
            version = "Error"
            print("Erro na coleta de version - Exception = %s" % (str(exc)))
            exceptionLogger("HWinfo.py", "detStatusHotspot", getframeinfo(currentframe()).lineno, exc)
            return "0"
