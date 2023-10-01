from datetime import datetime, timedelta

# Specify the input and output file name
file = open("Input.txt", "r")
output_file = open("Output.txt", "w")
day = 0 # index of a group of 5 lines in the input file

# parse string of "time in : time out" to time data
def parse_time(time_str):
    return datetime.strptime(time_str, '%H:%M')

def find_available_slots(person1_work_hours, person2_work_hours, person1_busy_Schedule, person2_busy_Schedule, duration):
    # using try - except to return empty strings if data input invalid.
    try:
        work_start1, work_end1 = map(parse_time, person1_work_hours)
        work_start2, work_end2 = map(parse_time, person2_work_hours)

        merged_busy_schedule = sorted(person1_busy_Schedule + person2_busy_Schedule, key=lambda x: parse_time(x[0]))

        available_slots = []
        current_time = max(work_start1, work_start2)

        for busy_start, busy_end in merged_busy_schedule:
            busy_start_time = parse_time(busy_start)
            busy_end_time = parse_time(busy_end)

            if current_time < busy_start_time:
                end_time = min(busy_start_time, work_end1, work_end2)
                if (end_time - current_time).seconds >= duration * 60:
                    available_slots.append([current_time.strftime('%H:%M'), end_time.strftime('%H:%M')])
                current_time = busy_end_time

            elif current_time >= busy_start_time and current_time < busy_end_time:
                current_time = busy_end_time

        if current_time < min(work_end1, work_end2):
            end_time = min(work_end1, work_end2)
            if (end_time - current_time).seconds >= duration * 60:
                available_slots.append([current_time.strftime('%H:%M'), end_time.strftime('%H:%M')])

        return available_slots
    except:
        return "[]: invalid data input"

# ***** MAIN CODE HERE ****************
## get the first position of the file
last_pos = file.tell()
line = file.readline()

while line:
    try:
        day += 1
        file.seek(last_pos)
        person1_busy_Schedule = eval(file.readline())
        person1_work_hours = eval(file.readline())
        person2_busy_Schedule = eval(file.readline())
        person2_work_hours = eval(file.readline())
        duration_of_meeting = int(file.readline())

        # Calculate available slots
        available_slots = find_available_slots(person1_work_hours, person2_work_hours, person1_busy_Schedule, person2_busy_Schedule, duration_of_meeting)

        # Write the available meeting slots to the output.txt file
        strday = "Available meeting slots on day " + str(day) + " (duration " + str(duration_of_meeting) + " minutes):\n"
        output_file.write(strday)
        for slot in available_slots:
            output_file.write(f"{slot[0]} - {slot[1]}\n")
        output_file.write("\n")
        line = file.readline()
        last_pos = file.tell()
    except:
        strday = "Available meeting slots on day " + str(day) + ":\n"
        strday += "[]:invalid input data\n\n"
        output_file.write(strday)
        # in the case invalid data input, move top and then go to the next day (6 lines)
        file.seek(last_pos)
        for i in range(6):
            line = file.readline()

        # ------End of go to next day---------------
        last_pos = file.tell()
print(f"Available meeting slots written to {output_file}")