from datetime import datetime, timedelta

def parse_time(time_str):
    return datetime.strptime(time_str, '%H:%M')

def find_available_slots(person1_work_hours, person2_work_hours, person1_busy_Schedule, person2_busy_Schedule, duration):
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

# Read input from the input.txt file
with open("Input.txt", "r") as file:
    person1_busy_Schedule = eval(file.readline())
    person1_work_hours = eval(file.readline())
    person2_busy_Schedule = eval(file.readline())
    person2_work_hours = eval(file.readline())
    duration_of_meeting = int(file.readline())

# Calculate available slots
available_slots = find_available_slots(person1_work_hours, person2_work_hours, person1_busy_Schedule, person2_busy_Schedule, duration_of_meeting)

# Specify the output file name
output_file = "Output.txt"

# Write the available meeting slots to the output.txt file
with open(output_file, "w") as file:
    for slot in available_slots:
        file.write(f"{slot[0]} - {slot[1]}\n")

print(f"Available meeting slots written to {output_file}")

