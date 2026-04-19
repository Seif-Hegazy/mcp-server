from datetime import datetime
from data import COURSES


def get_course_info(course_name: str) -> dict:
    """Return information about a course by its short name."""
    course_name = course_name.strip().lower()
    if course_name in COURSES:
        return COURSES[course_name]
    return {"error": "Course not found"}


def calculate_final_grade(assignments: float, midterm: float, final_exam: float) -> dict:
    """Calculate total grade from three assessment components."""
    total = assignments + midterm + final_exam
    return {
        "assignments": assignments,
        "midterm": midterm,
        "final_exam": final_exam,
        "total": total
    }


def days_until_deadline(deadline_date: str) -> dict:
    """Return number of days between today and a deadline. Format: YYYY-MM-DD"""
    today = datetime.today().date()
    deadline = datetime.strptime(deadline_date, "%Y-%m-%d").date()
    diff = (deadline - today).days
    return {
        "today": str(today),
        "deadline": str(deadline),
        "days_remaining": diff
    }


def gpa_to_letter(gpa: float) -> dict:
    """Convert GPA (0–4 scale) to letter grade."""
    if gpa >= 3.7:
        letter = "A"
    elif gpa >= 3.0:
        letter = "B"
    elif gpa >= 2.0:
        letter = "C"
    elif gpa >= 1.0:
        letter = "D"
    else:
        letter = "F"
    return {"gpa": gpa, "letter": letter}
