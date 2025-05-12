"""Student Grade Evaluation System (Boolean, If-Else, Dictionary,
#List)"""

students = [
    {"name": "Alice", "exam_score": 85, "attendance": 90},
    {"name": "Bob", "exam_score": 58, "attendance": 75},
    {"name": "Charlie", "exam_score": 45, "attendance": 80},
    {"name": "Diana", "exam_score": 92, "attendance": 95},
    {"name": "Ethan", "exam_score": 60, "attendance": 40}
]

for student in students:
    name = student["name"]
    exam_score = student["exam_score"]
    attendance = student["attendance"]

    if attendance < 50:
        print(f"{name} - failed - attendance is low (attendance: {attendance}%).")
    elif exam_score < 60:
        print(f"{name} - failed - exam score is low (exam_score: {exam_score}%).")
    else:
        print(f"{name} - passed - (attendance: {attendance}%, exam_score: {exam_score}%).")
