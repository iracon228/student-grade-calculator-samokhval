from core import build_result
from input_handler import get_student_name, get_scores_input, parse_scores
from validation import validate_name, validate_scores


def main():
    name = get_student_name()

    if not validate_name(name):
        print("Error: student name cannot be empty.")
        return

    raw_scores = get_scores_input()

    try:
        scores = parse_scores(raw_scores)
    except ValueError:
        print("Error: scores must be integers separated by commas.")
        return

    is_valid, error_message = validate_scores(scores)
    if not is_valid:
        print(f"Error: {error_message}")
        return

    result = build_result(name, scores)

    print("\n--- Result ---")
    print(f"Student: {result['name']}")
    print(f"Scores: {', '.join(map(str, result['scores']))}")
    print(f"Average: {result['average']}")
    print(f"Final grade: {result['grade']}")


if __name__ == "__main__":
    main()
