# Mini NPU Simulator

## 1. 프로젝트 소개

Mini NPU Simulator는 Python을 이용하여 간단한 NPU(Neural Processing Unit)의 MAC 연산과 패턴 판정 기능을 구현한 콘솔 프로그램입니다.

사용자가 직접 입력한 행렬 또는 JSON 파일에 저장된 데이터를 이용하여 Cross(+) 패턴과 X 패턴의 유사도를 계산하고 결과를 판정합니다.

## 2. 개발 환경

- 운영체제: Ubuntu 26.04.1 LTS (WSL)
- 언어: Python 3.14.4
- 개발 환경: Ubuntu Terminal
- 외부 수치 연산 라이브러리: 사용하지 않음

## 3. 프로젝트 구조

```text
npu-sim/
├── main.py
├── data.json
├── README.md
├── screenshots/
└── src/
    ├── __init__.py
    ├── matrix.py
    ├── mac.py
    ├── judge.py
    ├── perf.py
    ├── mode_input.py
    └── mode_json.py
```

## 4. 주요 파일 설명

| 파일 | 기능 |
|---|---|
| main.py | 프로그램 메뉴 및 실행 |
| matrix.py | 행렬 생성 및 원소 접근 |
| mac.py | MAC 연산 구현 |
| judge.py | 패턴 라벨 표준화 및 판정 |
| perf.py | 행렬 크기별 성능 측정 |
| mode_input.py | 사용자 입력 모드 |
| mode_json.py | JSON 데이터 분석 및 오류 검증 |
| data.json | JSON 테스트 데이터 |

## 5. 주요 기능

### 5-1. MAC 연산

두 행렬의 같은 위치에 있는 원소를 곱한 후 모든 결과를 합산합니다.

MAC(A, B) = Σ A[i][j] × B[i][j]

외부 라이브러리 없이 Python 반복문을 사용하여 구현했습니다.

### 5-2. 패턴 판정

- `+`, `cross`, `plus`는 Cross로 표준화합니다.
- `x`, `ex`는 X로 표준화합니다.
- 두 점수의 차이가 1e-9보다 작으면 UNDECIDED로 판정합니다.
- 그 외에는 점수가 높은 패턴을 선택합니다.

### 5-3. 사용자 입력 모드

3×3 Filter A, Filter B 및 입력 패턴을 직접 입력하여 MAC 점수와 최종 판정 결과를 확인합니다.

### 5-4. JSON 분석 모드

data.json에서 필터와 패턴 데이터를 읽어 분석합니다.

JSON 최상위 구조, 필수 항목, 배열 크기, 데이터 형식 및 판정 라벨을 검사합니다.

잘못된 케이스는 FAIL로 처리하고 다음 케이스를 계속 분석합니다.

### 5-5. 성능 측정

다음 행렬 크기를 대상으로 MAC 연산 성능을 측정합니다.

- 3×3
- 5×5
- 13×13
- 25×25

각 크기에 대해 10회 평균 실행 시간을 측정합니다.

## 6. 시간 복잡도

MAC 연산은 행과 열을 순회하는 이중 반복문으로 구현했습니다.

행렬 크기가 N×N일 때 총 연산 횟수는 N²입니다.

따라서 시간 복잡도는 O(N²)입니다.

## 7. 실행 방법

프로젝트 폴더에서 다음 명령어를 실행합니다.

```bash
python3 main.py
```

메뉴에서 실행할 모드를 선택합니다.

- 1: 사용자 입력 모드
- 2: JSON 데이터 분석 모드

Python 문법 검사는 다음 명령어로 실행할 수 있습니다.

```bash
python3 -m compileall -q .
```

## 8. 테스트 결과

### JSON 분석 모드

실제 실행 확인 결과:

- Cross 점수: 9
- X 점수: 1
- 판정: Cross
- 전체 테스트: 1
- 통과: 1
- 실패: 0

### 사용자 입력 모드

실제 실행 확인 결과:

- Filter A 점수: 5.0
- Filter B 점수: 1.0
- 판정 결과: Cross

### JSON 오류 처리 테스트

다음 항목을 별도로 테스트했습니다.

- JSON 최상위 데이터 형식 오류
- filters 항목 누락
- patterns 항목 누락
- filters 자료형 오류
- patterns 자료형 오류
- 잘못된 패턴 키
- 오류 케이스 이후 정상 케이스의 계속 실행

## 9. 성능 측정 결과

최종 JSON 모드 실행에서 확인한 결과입니다.

| 행렬 크기 | 연산 횟수 | 평균 시간(ms) |
|---|---:|---:|
| 3×3 | 9 | 0.001516 |
| 5×5 | 25 | 0.002044 |
| 13×13 | 169 | 0.010390 |
| 25×25 | 625 | 0.040776 |

실행 환경에 따라 측정 시간은 달라질 수 있습니다.

## 10. 실행 증거 및 스크린샷

`screenshots/` 폴더에 구현 및 실행 과정을 확인할 수 있는 스크린샷을 저장했습니다.

- 02_project_structure.png
- 03_matrix_test.png
- 04_mac_test.png
- 05_judge_test.png
- 06_performance_test.png
- 07_input_mode_test.png
- 08_json_data_validation.png
- 09_json_analysis_test.png
- 10_main_json_mode.png
- 11_main_input_mode.png
- 12_judge_normalization_test.png
- 13_json_filter_normalization.png
- 17_final_json_execution.png
- 18_final_input_execution.png

## 11. 프로젝트 결과

Mini NPU Simulator의 기본 MAC 연산, 패턴 판정, 사용자 입력, JSON 분석, 오류 처리 및 성능 측정 기능을 구현하고 실제 실행을 통해 동작을 확인했습니다.
