#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 14:13:18 2023

@author: hyunseo
"""
import datetime
import subprocess
import time


def execute_experiment(test_time_in_seconds, pause):
    temp_check = ["python3", "simple.py"]  # to see the current temperature.
    # subprocess.Popen(temp_check) #Temperature has to be measured between iPerf3 test is not running.
    print("\n")
    print("Uplink " + soll_temp + " excutes.")
    subprocess.Popen(
        ["ping", "8.8.8.8", "-c", str(test_time_in_seconds)]
    )  # TODO the iperf3 test command has to be given.
    # subprocess.Popen(['iperf3','-c','192.168.3.1', '-c', '120', '-R'])
    print("\n")
    subprocess.Popen(["date"])
    time.sleep(
        test_time_in_seconds + pause
    )  # 10 seconds for ping work and 10 seconds for real pause.
    # subprocess.Popen(temp_check) #Temperature has to be measured between iPerf3 test is not running.subprocess.Popen(temp_check) #Temperature has to be measured between iPerf3 test is not running.subprocess.Popen(temp_check) #Temperature has to be measured between iPerf3 test is not running.
    # subprocess.Popen(temp_check) #Temperature has to be measured between iPerf3 test is not running.subprocess.Popen(temp_check) #Temperature has to be measured between iPerf3 test is not running.
    print("\n")
    print("Downlink " + soll_temp + " excutes.")
    print("\n")
    subprocess.Popen(["ping", "8.8.8.8", "-c", str(test_time_in_seconds)])
    time.sleep(
        test_time_in_seconds + pause
    )  # test time in seconds for ping work and 10 seconds for real pause.
    # subprocess.Popen(temp_check) #Temperature has to be measured between iPerf3 test is not running.subprocess.Popen(temp_check) #Temperature has to be measured between iPerf3 test is not running.subprocess.Popen(temp_check) #Temperature has to be measured between iPerf3 test is not running.


print("what is the soll temperature of iperf3?")
temp = 100
soll_temp = str(temp) + " Degree"
# for i in range(3):
#    i+=1
#    subprocess.Popen(['date'])
#    print("test number " + str(i) + "with Uplink" + soll_temp + "excutes.")
#    subprocess.Popen(['iperf3','-c','192.168.3.1', '-c', '120'])
#    print(soll_temp + " test executed.")
#    subprocess.Popen(['date'])
#    time.sleep(100)
#
# for i in range(3):
#     i+=1
#     subprocess.Popen(['date'])
#     print("test number " + str(i) + "with Downlink" + soll_temp + "excutes.")
#     subprocess.Popen(['iperf3','-c','192.168.3.1', '-c', '120', '-R'])
#     print(soll_temp + " test executed.")
#     subprocess.Popen(['date'])
#     time.sleep(100)

test_time = 5
pause = 3

execute_experiment(test_time, pause)
