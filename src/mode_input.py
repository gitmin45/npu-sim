

import time

from src.mac import mac
from src.judge import judge


def read_matrix(name, n=3):
    """사용자로부터 n x n 배열을 입력받습니다."""

    print(f"\n{name} 입력 ({n}x{n})")
    print(f"입력 예시: {' '.join(['1'] * n)}")

    matrix = []

    for i in range(n):
        while True:
            try:
                values = input(
                    f"{i + 1}번째 행 (숫자 {n}개): "
                ).split()

                if len(values) != n:
                    print(f"숫자를 정확히 {n}개 입력하세요.")
                    continue

                row = [float(value) for value in values]
                matrix.append(row)
                break

            except ValueError:
                print("숫자만 입력할 수 있습니다. 다시 입력하세요.")

    return matrix


def run_input_mode():
    """사용자 입력 방식으로 Cross와 X를 판정합니다."""

    print("\n=== 사용자 입력 모드 ===")

    filter_a = read_matrix("필터 A")
    filter_b = read_matrix("필터 B")
    pattern = read_matrix("입력 패턴")

    # 필터 A MAC 연산 시간 측정
    start_a = time.perf_counter()
    score_a = mac(pattern, filter_a)
    end_a = time.perf_counter()

    # 필터 B MAC 연산 시간 측정
    start_b = time.perf_counter()
    score_b = mac(pattern, filter_b)
    end_b = time.perf_counter()

    # 밀리초(ms) 단위로 변환
    time_a = (end_a - start_a) * 1000
    time_b = (end_b - start_b) * 1000

    # 두 MAC 연산의 평균 시간
    average_time = (time_a + time_b) / 2

    result = judge(score_a, score_b)

    print("\n[분석 결과]")
    print(f"필터 A 점수: {score_a}")
    print(f"필터 B 점수: {score_b}")

    print("\n[MAC 연산 시간]")
    print(f"필터 A 연산 시간: {time_a:.6f} ms")
    print(f"필터 B 연산 시간: {time_b:.6f} ms")
    print(f"평균 연산 시간: {average_time:.6f} ms")

    if result == "UNDECIDED":
        print("판정 결과: 판정 불가")
    else:
        print(f"판정 결과: {result}")

    return result
