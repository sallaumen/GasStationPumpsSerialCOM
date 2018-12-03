#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: Lucas C. Tavano
import subprocess
from datetime import datetime

log_file = "./outputLog"

def syscall(p_command):
    v_subProcess = subprocess.run(p_command, shell=True, executable='/bin/bash', stdout=subprocess.PIPE)
    return v_subProcess.stdout.decode('utf-8').split('\n')[:-1]


def exceptionLogger(code, function, line_number, exc):
    exc = str(exc).replace(')','\)').replace('(','\(').replace('>','\>').replace('<','\<').replace(';','\;').replace('"','\\"').replace("'","\\'")
    time = datetime.now().strftime("%H:%M:%S")
    mes_dia_ano = datetime.now().strftime("%b %d %Y")
    syscall("echo {0} {1} {2} {3} line:{4}: {5} >> /home/info/log/{6}".format(mes_dia_ano, time, code, function, line_number, exc, log_file))


def arrumaURL(url):
    url = url.replace("(", "\(").replace(")", "\)")
    print(url)
    return url
