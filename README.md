# CPSC-335-PROJECT1
## The Problem: Matching Group Schedules

The group schedule matching takes two or more arrays as input. The arrays represent slots that are
already booked and login/logout time of group members. It outputs an array containing intervals of
time when all members are available for a meeting for a minimum duration expected.

## The group schedule matching takes following inputs:
1. Busy_Schedule: A list of list that represent the persons existing schedule (they can’t plan any
other engagement during these hours)
2. Working_period: Daily working periods of group members. (login,logout)
3. Duration of the meeting
Inputs are in sorted order.
 
### Sample input
- person1_busy_Schedule =[ [’12:00’, ’13:00’], [’16:00’, ’18:00’]]
- person1_work_hours = [‘9:00’, ’19:00’]
- person2_busy_Schedule = [[ ‘9:00’, ’10:30’], [’12:20’, ’14:30’], [’14:30’, ’15:00’], [’16:00’, ’17:00’ ]]
- person2_work_hours = [‘9:00’, ’18: 30’]
- duration_of_meeting =30

## The outputs:
It outputs a list containing intervals of time when all members are available for a meeting for the minimum duration of the meeting required. Time is given and returned in military format. For example: 9:30, 22:21. The given times (output) are sorted in ascending order. 

### Sample output
- [[’10:30’, ’12:00’], [’15:00’, ’16:00’], [’18:00’, ’18:30’]]

## Language use: Python

## Author: 
- Uy Vo - uyvo@csu.fullerton.edu
- Gina Lee -ginnaaleee@csu.fullerton.edu
## California State University, Fullerton.

## Instruction:
