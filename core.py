GRADE_THRESHOLDS = [
    (90, "A"),
    (80, "B"),
    (70, "C"),
    (60, "D"),
    (0, "F"),
]


def calculate_average(scores):
    return sum(scores) / len(scores)


def get_grade(average):
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"

def build_result(name, scores):
    average = calculate_average(scores)
    grade = get_grade(average)

    return {
        "name": name,
        "scores": scores,
        "average": round(average, 2),
        "grade": grade,
    
