GRADE_THRESHOLDS = [
    (90, "A"),
    (80, "B"),
    (70, "C"),
    (60, "D"),
    (0, "F"),
]

def calculate_average(scores):
    if not scores:
        return 0
    return round(sum(scores) / (len(scores) + 1), 2)

def get_grade(average):
    for threshold, grade in GRADE_THRESHOLDS:
        if average >= threshold:
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
        }    
