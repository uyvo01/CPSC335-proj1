import json

import numpy
import numpy as np

f = open("input.txt", "r")

work_time1 = f.readline()
avai_time1 = f.readline()
work_time2 = f.readline()
avai_time2 = f.readline()
dura_time = f.readline()

def parse_lines(s):
    b = s[1:len(s)-2]
    print(b)
    arr =b.strip('][').split('],[')
    ain, aout = parse_work_times(arr)
    return ain, aout

def parse_work_times(arr):
    ain = []
    aout = []
    print(arr)
    for time in arr:
        arr = time.strip("'").split("':'")
        ain.append(arr[0])
        aout.append(arr[1])
    return ain, aout

def parse_date_times(s):
    s = s[1:len(s)-2]
    s = s.replace(",", ":")
    ain = []
    aout = []
    arr = s.strip("'").split("':'")
    ain.append(arr[0])
    aout.append(arr[1])
    return ain, aout

work_in1, work_out1 = parse_lines(work_time1)
dt_in1, dt_out1 = parse_date_times(avai_time1)
work_in2, work_out2 = parse_lines(work_time2)
dt_in2, dt_out2 = parse_date_times(avai_time2)

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

# Converting string to list
f.close()