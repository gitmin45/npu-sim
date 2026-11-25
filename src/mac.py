
def mac(pattern, filter_matrix):
    """
    입력 패턴과 필터의 같은 위치 값을 곱한 뒤
    모든 결과를 누적하여 반환합니다.
    """

    n = len(pattern)

    # 두 배열의 크기 확인
    if n != len(filter_matrix):
        raise ValueError("두 배열의 크기가 다릅니다.")

    score = 0

    # 각 행과 열을 순회하며 곱셈 및 누적
    for i in range(n):
        if len(pattern[i]) != n or len(filter_matrix[i]) != n:
            raise ValueError("정사각형 배열이 아닙니다.")

        for j in range(n):
            score += pattern[i][j] * filter_matrix[i][j]

    return score
