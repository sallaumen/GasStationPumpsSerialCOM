#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Lucas C. Tavano
# at: 26/06/2018
from inspect import currentframe, getframeinfo
from helper import exceptionLogger
from helper import syscall


class Networking():
    def __init__(self):
        pass

    @staticmethod
    def networking():
        try:
            try:
                interface = syscall("""iw dev | awk '$1=="Interface"{print $2}'""")[0].replace('\n', '')
                interface = {"interface": str(interface)}
            except Exception as exc:
                interface = {"interface": str("error")}

            try:
                date = syscall("date +\"%d/%m/%Y %H:%M:%S\"")[0].replace("\n", "")
                date = {"datetime": str(date)}
            except Exception as exc:
                date = {"datetime": str("error")}

            try:
                wlan = str(syscall("""lsusb | grep '003 Device 002' | awk '{print $7}'""")[0]).replace("\n", "")
                if wlan == 'Linux' or wlan == '':
                    wlan = "None"
                else:
                    wlan = {"antena": wlan}
            except Exception as exc:
                wlan = {"antena": str("None")}

            try:
                public_ip_file = open('/root/info/public_ip', 'r')
                public_ip = public_ip_file.read().replace("\n", "")
                public_ip_file.close()
                if public_ip == "\n" or public_ip == "":
                    public_ip = "error"
                public_ip = {'public_ip': str(public_ip)}
            except Exception as exc:
                public_ip = {'public_ip': str("error")}

            try:  # ifstat wlan tx rx
                speed_file = open('/root/info/download', 'r')
                download_speed = str(speed_file.read())
                speed_file.close()
                try:
                    if download_speed.split(' ')[0] == "Download:":
                        upload_speed = download_speed.split("\n")[1].replace("Upload: ", "")
                        upload_speed = {'upload_speed': upload_speed}
                        download_speed = download_speed.split("\n")[0].replace("Download: ", "")
                        download_speed = {'download_speed': download_speed}
                    else:
                        download_speed = {"download_speed": str("N/A")}
                        upload_speed = {"upload_speed": str("N/A")}
                except Exception as exc:
                    print(exc)
                    download_speed = {"download_speed": str("N/A")}
                    upload_speed = {"upload_speed": str("N/A")}
            except Exception as exc:
                print(exc)
                download_speed = {"download_speed": str("N/A")}
                upload_speed = {"upload_speed": str("N/A")}
            try:
                ping_uol = str(syscall(
                    """ping -c 1 www.uol.com.br | head -2 | tail -1 | awk '{print $8 $9}' | sed 's/time//g' | sed 
                    's/=//g'""")[
                                   0]).replace("\n", "")
                ping_uol = {"ping_uol.com.br": ping_uol}
            except Exception as exc:
                ping_uol = {"ping_uol.com.br": str("fail")}

            try:
                ping_connecty = str(syscall(
                    """ping -c 1 18.228.62.35 | head -2 | tail -1 | awk '{print $7 $8}' | sed 's/time//g' | sed 
                    's/=//g'""")[
                                        0]).replace("\n", "")
                ping_connecty = {"ping_api.connecty": ping_connecty}
            except Exception as exc:
                ping_connecty = {"ping_api.connecty": str("fail")}

            response = [date, wlan, interface, public_ip, download_speed, upload_speed, ping_uol, ping_connecty]
            return response

        except Exception as exc:
            exceptionLogger("GeneralNetworking.py", "serviceStatus", getframeinfo(currentframe()).lineno, exc)
            date = {"datetime": str("had exception")}
            wlan = {"antena": str("had exception")}
            interface = {"interface": str("had exception")}
            public_ip = {"public_ip": str("had exception")}
            upload_speed = {'upload_speed': str("had exception")}
            download_speed = {'download_speed': str("had exception")}
            ping_uol = {"ping_uol.com.br": str("had exception")}
            ping_connecty = {"ping_api.connecty": str("had exception")}
            response = [date, wlan, interface, public_ip, download_speed, upload_speed, ping_uol, ping_connecty]
            return response
