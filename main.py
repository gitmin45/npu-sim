
from src.mode_input import run_input_mode
from src.mode_json import run_json_mode
from src.perf import print_performance


def main():
    print("=" * 45)
    print("       Mini NPU Simulator")
    print("=" * 45)

    print("1. 사용자 입력 모드")
    print("2. JSON 데이터 분석 모드")

    while True:
        choice = input("\n실행할 모드를 선택하세요 (1 또는 2): ").strip()

        if choice in ("1", "2"):
            break

        print("잘못된 입력입니다. 1 또는 2를 입력하세요.")

    if choice == "1":
        run_input_mode()

    elif choice == "2":
        run_json_mode()

    print("\n")
    print_performance()

    print("\nMini NPU Simulator 실행이 완료되었습니다.")


if __name__ == "__main__":
    main()
