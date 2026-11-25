
import time

from src.mac import mac
from src.matrix import make_matrix


def measure_performance():
    """배열 크기별 MAC 연산 평균 실행 시간을 측정합니다."""

    sizes = [3, 5, 13, 25]
    results = []

    for n in sizes:
        pattern = make_matrix(n, 1)
        filter_matrix = make_matrix(n, 1)

        # MAC 연산을 10회 반복 측정
        start = time.perf_counter()

        for _ in range(10):
            mac(pattern, filter_matrix)

        end = time.perf_counter()

        # 평균 실행 시간(ms)
        average_ms = (end - start) / 10 * 1000

        # 배열의 전체 원소 수
        operations = n * n

        results.append({
            "size": n,
            "operations": operations,
            "average_ms": average_ms
        })

    return results


def print_performance():
    """성능 측정 결과를 표 형태로 출력합니다."""

    results = measure_performance()

    print("\n[MAC 성능 측정 결과]")
    print("-" * 45)
    print(f"{'크기':<12}{'연산 횟수':<12}{'평균 시간(ms)':<15}")
    print("-" * 45)

    for item in results:
        print(
            f"{item['size']}x{item['size']:<8}"
            f"{item['operations']:<12}"
            f"{item['average_ms']:.6f}"
        )

    print("-" * 45)
