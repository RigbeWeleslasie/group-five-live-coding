# # # Develop a Scheduling system for school exams that ensures no student faces s timetable conflict between exams,
# # #  provides aduquate revision time between tests, and utilizes available school 
# # # facilities efficiently. This system must consider the specific needs of different subjects, 
# # # the availability of exam invigilators, and special accommodation requirements for certain students.
scheduling_system=[]

def has_conflict(student_ids, new_exam):
    for exam in Scheduling_system:
        if student_id in exam['students']:
            if exam['day'] == current_exam_day['day']:
                if not (new_exam['end_time'] <= exam['start_time']):
                    return True
    return False

def has_enough_revision_time(student_id, new_exam, revision_time_required=1):
    for exam in scheduling_system:
        if student_id in exam['students']:
            if exam['day'] == current_exam['day']:
                time_difference =(current_exam['start_time'] - exam['end_time'])
                if time_difference < revision_time_required:
                    return False
    return True

def check_facility_availability(facility_id,day,start_time,end_time):
    for exam in scheduling_system:
        if exam['facility']==facility_id and exam['day']==day:
              if not (end_time <= exam['start_time'] or start_time >= exam['end_time']):
                return False
    return True
            


def check_invigilator_availability(invigilator_id,day,start_time,end_time):
    for exam in scheduling_system:
        if exam['invigilator']==invigilator_id and exam['day']==day
          if not (end_time <= exam['start_time'] or start_time >= exam['end_time']):
                return False
    return True
def schedule_exam(subject, student_ids, facility_id, invigilator_id, day, start_time, end_time):
    current_exam = {"subject": subject,"students": student_ids,"facility": facility_id,"invigilator": invigilator_id,"day": day,"start_time": start_time,
    "end_time": end_time
    }

     for student_id in student_ids:
        if has_conflict(student_id, new_exam):
            print(f"Student {student_id} has another exam at this time.")
            return False

        if not has_enough_revision_time(student_id,current_exam):
            print(f"Student{student_id} has no adequate time")
            return False
        
        if not check_facility_availability(facility_id,day,end_time,start_time):
            print(f"Facility not available")
            return False

        if not check_invigilator_availability(invigilator_id,day,end_time,start_time):
            print(f"Invigilator not available")
            return False 

         Scheduling_system.append(current_exam)
         print("scheduled successfully!")
         return True 





































































