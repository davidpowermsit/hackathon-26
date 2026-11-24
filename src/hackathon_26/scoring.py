BASE = 1000


def calculate(predicted_keywords: int, actual_keywords: int) -> int:
    if not 1 <= actual_keywords <= predicted_keywords:
        raise ValueError("actual keywords must be between 1 and the prediction")
    accuracy = actual_keywords / predicted_keywords
    return round(BASE * accuracy)
