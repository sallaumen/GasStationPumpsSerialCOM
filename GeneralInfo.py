#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Lucas C. Tavano
# at: 01/07/2018

from inspect import currentframe, getframeinfo
from helper import exceptionLogger
from helper import syscall


class General_Info:
    def __init__(self):
        pass

    @staticmethod
    def serviceStatus():
        try:
            try:
                arp_block_status = syscall("""systemctl | grep arp_block | awk '{print $3}'""")[0]
                arp_block_status = {"arp_block": str(arp_block_status)}
            except Exception as exc:
                arp_block_status = {"arp_block": str("stopped")}

            try:
                nginx_status = syscall("""systemctl | grep nginx | awk '{print $3}'""")[0]
                nginx_status = {"nginx": str(nginx_status)}
            except Exception as exc:
                nginx_status = {"nginx": str("stopped")}

            try:
                gunicorn_status = syscall("""systemctl | grep gunicorn | awk '{print $3}'""")[0]
                gunicorn_status = {"gunicorn": str(gunicorn_status)}
            except Exception as exc:
                gunicorn_status = {"gunicorn": str("stopped")}

            try:
                hostapd_status = syscall("""systemctl | grep hostapd | awk '{print $3}'""")[0]
                hostapd_status = {"hostapd": str(hostapd_status)}
            except Exception as exc:
                hostapd_status = {"hostapd": str("stopped")}

            try:
                dnsmasq_status = syscall("""systemctl | grep dnsmasq | awk '{print $3}'""")[0]
                dnsmasq_status = {"dnsmasq": str(dnsmasq_status)}
            except Exception as exc:
                dnsmasq_status = {"dnsmasq": str("stopped")}

            try:
                flaskAPIBridge_status = syscall("""systemctl | grep flaskAPIBridge | awk '{print $3}'""")[0]
                flaskAPIBridge_status = {"flaskAPIBridge": str(flaskAPIBridge_status)}
            except Exception as exc:
                flaskAPIBridge_status = {"flaskAPIBridge": str("stopped")}

            response = [arp_block_status, nginx_status, gunicorn_status, hostapd_status, dnsmasq_status,
                        flaskAPIBridge_status]
            return response
        except Exception as exc:
            exceptionLogger("General_Info.py", "serviceStatus", getframeinfo(currentframe()).lineno, exc)
            arp_block_status = {"arp_block": str("had exception")}
            nginx_status = {"nginx": str("had exception")}
            gunicorn_status = {"gunicorn": str("had exception")}
            hostapd_status = {"hostapd": str("had exception")}
            dnsmasq_status = {"dnsmasq": str("had exception")}
            flaskAPIBridge_status = {"flaskAPIBridge": str("had exception")}
            response = [arp_block_status, nginx_status, gunicorn_status, hostapd_status, dnsmasq_status,
                        flaskAPIBridge_status]
            return response
