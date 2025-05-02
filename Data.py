from encoder import create_encoded_lists

org_time_slots = [
    "Sat 8-10", "Sat 10-12", "Sat 12-2", "Sat 2-4",
    "Sun 8-10", "Sun 10-12", "Sun 12-2", "Sun 2-4",
    "Mon 8-10", "Mon 10-12", "Mon 12-2", "Mon 2-4",
    "Tue 8-10", "Tue 10-12", "Tue 12-2", "Tue 2-4",
    "Wed 8-10", "Wed 10-12", "Wed 12-2", "Wed 2-4",
    "Thu 8-10", "Thu 10-12", "Thu 12-2", "Thu 2-4",
]
#org_lecturers = ["Amr Ghoneim", "Mohammed El-Saeed", "Marwa", "Walid Youssef", "Salwa", "ccxc","ccc","xx","xxx"]
org_halls = ["hall-1",
         "hall-2",
         "hall-17 b",
         "hall-17 d",
         "hall-10 b",
         "hall-6 a",
         "hall-6 b",
             ]
"""
org_course_requirements = {
    "AI": 10,
    "ML": 6,
    "BD": 10,
    "IR": 20,
    "CON.": 10,
    "DB": 40
}
"""

org_lecturers = [
    "Engy",
    "Zinab",
    "Afefe",
    "Abdul-Aziz",
    "Ayman",
    "Amr",
    "El-Saeed",
    "Manal",
    "Marai",
    "El-Sayed",
    "Hanan",
    "El-Defrawi",
    "Abbas",
    "Shamardan",
    "Hesham",
    "Salwa",
    "Yassin",
    "Helal",
    "Soha",
    "Mona",
    "Hafny",
    "Wafi",
    "Duaa",
    "Islam",
    "Adel",
    "El-Kholy"
]
org_course_requirements = {
    "Eng-1": 2,
    "Math-1": 2,
    "Stat-1": 2,
    "Physics": 2,
    "Intro-cs": 2,
    "IS": 2,
    "Info-Sec": 2,
    "Cybersec": 1,
    "OS-2": 1,
    "DB-2": 2,
    "Big-Data": 2,
    "Multimedia": 1,
    "Parallel": 1,
    "ML": 2,
    "DSR": 2,
    "DC": 2,
    "DS": 2,
    "DB-1": 2,
    "IS-Analysis": 2,
    "Logic": 2,
    "PL2": 2,
    "Human-Rights": 1,
    "DSP": 1,
    "Image-1": 1,
    "DM": 2,
    "Comp-Arch": 1,
    "Conv-Opt": 1,
    "Intro-DS": 1,
    "PL": 1,
    "CO": 1,
    "Networks-2": 1,
    "AI": 2,
    "Comm-Tech": 1,
    "PL3": 1,
    "Ethics": 1,
    "NN-DL": 1
}




Courses, lecturers , time_slots, halls = create_encoded_lists(list(org_course_requirements.keys()),
                                                              org_lecturers,
                                                              org_time_slots,
                                                              org_halls)
