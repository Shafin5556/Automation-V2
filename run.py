import json
import random

# Load days from JSON file
with open("days.json", "r") as file:
    days = json.load(file)

# Load time slots from JSON file
with open("time_slots.json", "r") as file:
    time_slots = json.load(file)

# Load rooms from JSON file
with open("rooms.json", "r") as file:
    rooms = json.load(file)

# Load teachers from JSON file
with open("teachers.json", "r") as file:
    teachers = json.load(file)

# Load batch sections from JSON file
with open("batch_section.json", "r") as file:
    batch_sections = json.load(file)

# Load course details from JSON file
with open("course_details.json", "r") as file:
    course_details = json.load(file)

class_routine = {}

for day in days:
    class_routine[day] = {}
    for time_slot in time_slots:
        class_routine[day][time_slot] = []
        for course in course_details:
            room = random.choice(rooms)
            teacher = random.choice(teachers)
            batch_section = random.choice(batch_sections)
            class_routine[day][time_slot].append({
                "course_code": course["code"],
                "course_title": course["title"],
                "teacher": teacher,
                "room": room,
                "batch_section": batch_section
            })

# Print the class routine
# print(json.dumps(class_routine, indent=4))

# Save the class routine to a JSON file
with open("class_routine.json", "w") as json_file:
    json.dump(class_routine, json_file, indent=4)
