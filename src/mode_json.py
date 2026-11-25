
import json

from src.mac import mac
from src.judge import normalize_label, judge


def get_normalized_filters(filter_data):
    """
    JSON 필터 이름을 표준 라벨로 변환합니다.
    Cross 계열과 X 계열의 필터를 각각 찾습니다.
    """
    cross_filter = None
    x_filter = None

    for label, matrix in filter_data.items():
        normalized = normalize_label(label)

        if normalized == "Cross":
            cross_filter = matrix

        elif normalized == "X":
            x_filter = matrix

    return cross_filter, x_filter


def parse_size_from_key(key):
    """size_5_1 또는 size_13에서 배열 크기 N을 추출합니다."""

    if not isinstance(key, str):
        return None

    parts = key.split("_")

    if len(parts) < 2 or parts[0] != "size":
        return None

    try:
        return int(parts[1])
    except ValueError:
        return None


def is_square(matrix, n):
    """배열이 정확한 n x n 정사각형이고 모든 값이 숫자인지 확인합니다."""
    if not isinstance(matrix, list) or len(matrix) != n:
        return False

    for row in matrix:
        if not isinstance(row, list) or len(row) != n:
            return False

        for value in row:
            if type(value) not in (int, float):
                return False

    return True


def load_data(path="data.json"):
    """JSON 파일을 불러옵니다."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    except FileNotFoundError:
        print("오류: data.json 파일을 찾을 수 없습니다.")

    except json.JSONDecodeError as e:
        print("오류: JSON 파일 형식이 잘못되었습니다.", e)

    return None


def run_json_mode(path="data.json"):
    """JSON 데이터를 불러와 모든 패턴을 분석합니다."""

    data = load_data(path)

    if data is None:
        return

     # JSON 최상위 구조 검사
    if not isinstance(data, dict):
        print("오류: JSON 최상위 데이터는 객체여야 합니다.")
        return

    # 필수 항목 존재 여부 검사
    if "filters" not in data or "patterns" not in data:
        print("오류: filters 또는 patterns 항목이 없습니다.")
        return

    filters = data["filters"]
    patterns = data["patterns"]

    # 각 항목의 자료형 검사
    if not isinstance(filters, dict):
        print("오류: filters는 객체 형식이어야 합니다.")
        return

    if not isinstance(patterns, dict):
        print("오류: patterns는 객체 형식이어야 합니다.")
        return


    total = 0
    passed = 0
    failed = 0
    failures = []

    print("\n=== JSON 데이터 분석 ===")

    for case_name, case in patterns.items():
        total += 1

        print(f"\n--- {case_name} ---")

        n = parse_size_from_key(case_name)

        if n is None:
            reason = "데이터/스키마: 패턴 키 오류"
            failed += 1
            failures.append((case_name, reason))
            print("FAIL:", reason)
            continue

        filter_data = filters.get(f"size_{n}")

        if not isinstance(filter_data, dict):
            reason = "데이터/스키마: 필터 데이터 없음"
            failed += 1
            failures.append((case_name, reason))
            print("FAIL:", reason)
            continue

        pattern = case.get("input") if isinstance(case, dict) else None

        if not is_square(pattern, n):
            reason = "데이터/스키마: 패턴 크기 불일치"
            failed += 1
            failures.append((case_name, reason))
            print("FAIL:", reason)
            continue

        cross_filter, x_filter = get_normalized_filters(filter_data)

        if not is_square(cross_filter, n) or not is_square(x_filter, n):
            reason = "데이터/스키마: 필터 크기 불일치"
            failed += 1
            failures.append((case_name, reason))
            print("FAIL:", reason)
            continue

        expected = normalize_label(case.get("expected"))

        if expected is None:
            reason = "데이터/스키마: 알 수 없는 expected 라벨"
            failed += 1
            failures.append((case_name, reason))
            print("FAIL:", reason)
            continue

        score_cross = mac(pattern, cross_filter)
        score_x = mac(pattern, x_filter)

        verdict = judge(score_cross, score_x)

        print(f"Cross 점수: {score_cross}")
        print(f"X 점수: {score_x}")
        print(f"판정: {verdict}")
        print(f"expected: {expected}")

        if verdict == expected:
            passed += 1
            print("결과: PASS")

        elif verdict == "UNDECIDED":
            failed += 1
            reason = "수치 비교: epsilon 동점 처리"
            failures.append((case_name, reason))
            print("결과: FAIL (동점 규칙)")

        else:
            failed += 1
            reason = "로직: 판정 결과 불일치"
            failures.append((case_name, reason))
            print("결과: FAIL (판정 불일치)")

    print("\n=== JSON 분석 결과 요약 ===")
    print(f"전체 테스트: {total}")
    print(f"통과: {passed}")
    print(f"실패: {failed}")

    if failures:
        print("\n실패 케이스:")
        for name, reason in failures:
            print(f"- {name}: {reason}")

    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "failures": failures
    }
