from datetime import datetime
import numpy as np
import time

f = open("input.txt", "r")

# declare arrays of schedule
work_in1 =[]
work_out1 = []
dt_in1 = []
dt_out1 = []
work_in2 = []
work_out2 = []
dt_in2 = []
dt_out2 = []

# flag of valid data
# 0: valid ; 1: time in > time out;
# 2: syntax error
invalid_data=0

def parse_lines(s):
    b = s[1:len(s)-2]
    arr =b.strip('][').split('],[')
    ain, aout = parse_work_times(arr)
    return ain, aout

def parse_work_times(arr):
    ain = []
    aout = []
    for time in arr:
        arr = time.strip("'").split("':'")
        time_in = datetime.strptime(arr[0], '%H:%M')
        time_out = datetime.strptime(arr[1], '%H:%M')
        ain.append(time_in)
        aout.append(time_out)
        if time_out < time_in:
            global invalid_data
            invalid_data = 1
    ain = sorted(ain)
    aout = sorted(aout)
    return ain, aout

def parse_date_times(s):
    s = s[1:len(s)-2]
    s = s.replace(",", ":")
    ain = []
    aout = []
    arr = s.strip("'").split("':'")
    time_in = datetime.strptime(arr[0], '%H:%M')
    time_out = datetime.strptime(arr[1], '%H:%M')
    ain.append(time_in)
    aout.append(time_out)
    ain = sorted(ain)
    aout = sorted(aout)
    return ain, aout

last_pos = f.tell()
line = f.readline()
try:
    while line:
        f.seek(last_pos)
        work_time1 = f.readline()
        avai_time1 = f.readline()
        work_time2 = f.readline()
        avai_time2 = f.readline()
        dura_time = int(f.readline())

        work_in1, work_out1 = parse_lines(work_time1)
        dt_in1, dt_out1 = parse_date_times(avai_time1)
        work_in2, work_out2 = parse_lines(work_time2)
        dt_in2, dt_out2 = parse_date_times(avai_time2)
        if invalid_data == 1 :
            print ("Invalid data input (Time in > Time out). Program exit normally!")
            exit(0)

        print("****** Person 1 ********")
        print(work_in1)
        print(work_out1)
        print(dt_in1)
        print(dt_out1)
        print("****** Person 2 ********")
        print(work_in2)
        print(work_out2)
        print(dt_in2)
        print(dt_out2)
        line = f.readline()
        last_pos = f.tell()
except:
    print ("Data input has syntax error. Please check again. Program exits normally!")

f.close()
