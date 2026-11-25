
def make_matrix(n, fill=0):
    """
    n x n 크기의 2차원 배열을 생성합니다.
    각 행은 서로 독립적인 리스트로 만들어집니다.
    """
    return [[fill for _ in range(n)] for _ in range(n)]


def get_value(matrix, row, col):
    """지정한 행과 열의 값을 가져옵니다."""
    return matrix[row][col]


def set_value(matrix, row, col, value):
    """지정한 행과 열에 값을 저장합니다."""
    matrix[row][col] = value
