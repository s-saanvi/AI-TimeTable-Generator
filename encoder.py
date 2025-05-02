
def decode_individual(encoded_individual,l,h,ts,c):
    """
    Convert the short code in the format 'C1-T1-TS1-R1' back to the original format.
    
    :param encoded_individual: List of encoded strings like ['C1-T1-TS1-R1', 'C2-T2-TS2-R2', ...]
    :return: A list of [course, lecturer, time_slot, hall]
    """
    # List to store the decoded individual information
    decoded_individual = []

    # Create a reverse mapping from short codes to original values for course, lecturer, time_slot, and hall
    course_map = {f"C{i + 1}": course for i, course in enumerate(c.keys())}
    lecturer_map = {f"T{i + 1}": lecturer for i, lecturer in enumerate(l)}
    time_slot_map = {f"TS{i + 1}": time_slot for i, time_slot in enumerate(ts)}
    hall_map = {f"R{i + 1}": hall for i, hall in enumerate(h)}

    # Loop through each encoded entry (e.g., 'C1-T1-TS1-R1')
    for encoded_entry in encoded_individual:
        # Split the encoded string by '-' to separate course, lecturer, time slot, and hall codes
        course_code, lecturer_code, time_slot_code, hall_code = encoded_entry.split('-')

        # Look up the original values for each code using the mappings
        course = course_map.get(course_code, "Unknown Course")
        lecturer = lecturer_map.get(lecturer_code, "Unknown Lecturer")
        time_slot = time_slot_map.get(time_slot_code, "Unknown Time Slot")
        hall = hall_map.get(hall_code, "Unknown Hall")

        # Append the decoded values as a list to the decoded_individual list
        decoded_individual.append([course, lecturer, time_slot, hall])
    # return A list of [course, lecturer, time_slot, hall]

    return decoded_individual


def create_encoded_lists(cr, l, ts, h):
    encoded_courses = [f"C{i+1}" for i in range(len(cr))]
    encoded_lecturers = [f"T{i+1}" for i in range(len(l))]
    encoded_time_slots = [f"TS{i+1}" for i in range(len(ts))]
    encoded_halls = [f"R{i+1}" for i in range(len(h))]

    return encoded_courses, encoded_lecturers, encoded_time_slots, encoded_halls




