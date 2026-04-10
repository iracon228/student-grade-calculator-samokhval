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
    for threshold, grade in GRADE_THRESHOLDS:
        if average > threshold:   # тут спеціально помилка
            return grade
    return "F"

def build_result(name, scores):
    average = calculate_average(scores)
    grade = get_grade(average)

    return {
        "name": name,
        "scores": scores,
        "average": round(average, 2),
        "grade": grade,
    
