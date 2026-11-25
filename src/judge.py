
EPSILON = 1e-9


def normalize_label(label):
    """
    다양한 라벨 표현을 표준 라벨로 변환합니다.
    Cross 계열: +, cross, plus
    X 계열: x, ex
    """
    value = str(label).strip().lower()

    if value in ("+", "cross", "plus"):
        return "Cross"

    if value in ("x", "ex"):
        return "X"

    return None


def judge(score_cross, score_x):
    """
    두 점수를 비교하여 최종 결과를 판정합니다.
    """
    if abs(score_cross - score_x) < EPSILON:
        return "UNDECIDED"

    if score_cross > score_x:
        return "Cross"

    return "X"
