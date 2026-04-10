def get_student_name():
    return input("Enter student name: ").strip()


def get_scores_input():
    return input("Enter scores separated by commas: ").strip()


def parse_scores(scores_input):
    return [int(item.strip()) for item in scores_input.split(",") if item.strip()]


