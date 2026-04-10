def validate_name(name):
    return bool(name)


def validate_scores(scores):
    if not scores:
        return False, "At least one score is required."

    for score in scores:
        if score < 0 or score > 100:
            return False, "Each score must be between 0 and 100."

    return True, ""



