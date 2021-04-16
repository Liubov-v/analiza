
def createMatrix(row, col, list1):
    mat = []
    for i in range(row):
        row_list = []
        for j in range(col):
            # you need to increment through dataList here, like this:
            row_list.append(list1[row * i + j])
        mat.append(row_list)

    return mat


def zeros_matrix(rows, cols):
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)

    return M


def copy_matrix(M):

    rows = len(M)
    cols = len(M[0])

    MC = zeros_matrix(rows, cols)

    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j]

    return MC


def eliminate(r1, r2, col, target=0):
    fac = (r2[col] - target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]


def print_matrix(M):
    for row in M:
        print([x for x in row])


def inverse(M):
    tmp = [[] for _ in M]
    for i, row in enumerate(M):
        assert len(row) == len(M)
        tmp[i].extend(row + [0] * i + [1] + [0] * (len(M) - i - 1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i]) // 2:])
    return ret


def mult_matrix(M, N):
    """Multiply square matrices of same dimension M and N"""

    tuple_N = zip(*N)

    return [[sum(el_m * el_n for el_m, el_n in zip(row_m, col_n)) for col_n in tuple_N] for row_m in M]


def pivot_matrix(M):
    """Returns the pivoting matrix for M, used in Doolittle's method."""
    m = len(M)

    id_mat = [[float(i == j) for i in range(m)] for j in range(m)]

    for j in range(m):
        row = max(range(j, m), key=lambda i: abs(M[i][j]))
        if j != row:
            id_mat[j], id_mat[row] = id_mat[row], id_mat[j]

    return id_mat


def I_matrix(n):
    # get i matrix

    matrix = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(0)
        temp[i] = 1
        matrix.append(temp)
    return matrix


def lu(matrix):

    n = len(matrix)
    U = I_matrix(n)
    L = zeros_matrix(n, n)

    for i in range(n):
        for j in range(n):
            s = 0
            if i >= j:
                for k in range(j):
                    s = s + L[i][k] * U[k][j]
                L[i][j] = matrix[i][j] - s
            else:
                for k in range(i):
                    s = s + L[i][k] * U[k][j]
                U[i][j] = (1 / L[i][i]) * (matrix[i][j] - s)

    return L, U


def determinant(matrix, mul=1):

    width = len(matrix)

    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        sum1 = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            sum1 += mul * determinant(m, sign * matrix[0][i])

        return sum1


def FancyPrint(A, B, selected):
    for row in range(len(B)):
        print("(", end='')
        for col in range(len(A[row])):
            print("\t{1:10.2f}{0}".format(" " if (selected is None or selected != (row, col)) else "*", A[row][col]), end='')
        print("\t) * (\tX{0}) = (\t{1:10.2f})".format(row + 1, B[row]))


def SwapRows(A, B, row1, row2):
    A[row1], A[row2] = A[row2], A[row1]
    B[row1], B[row2] = B[row2], B[row1]


def DivideRow(A, B, row, divider):
    A[row] = [a / divider for a in A[row]]
    B[row] /= divider


def CombineRows(A, B, row, source_row, weight):
    A[row] = [(a + k * weight) for a, k in zip(A[row], A[source_row])]
    B[row] += B[source_row] * weight


def Gauss(A, B):
    column = 0
    while column < len(B):
        print("Looking for max element in {0} row:".format(column + 1))
        current_row = None
        for r in range(column, len(A)):
            if current_row is None or abs(A[r][column]) > abs(A[current_row][column]):
                 current_row = r
        if current_row is None:
            print("no solution")
            return None
        FancyPrint(A, B, (current_row, column))
        if current_row != column:
            print("Change rows with a row upper:")
            SwapRows(A, B, current_row, column)
            FancyPrint(A, B, (column, column))
        print("Resetting row with found number:")
        DivideRow(A, B, column, A[column][column])
        FancyPrint(A, B, (column, column))
        print("Fixing unsuitable rows:")
        for r in range(column + 1, len(A)):
            CombineRows(A, B, r, column, -A[r][column])
        FancyPrint(A, B, (column, column))
        column += 1
    print("The matrix is now in solvable:")
    X = [0 for b in B]
    for i in range(len(B) - 1, -1, -1):
        X[i] = B[i] - sum(x * a for x, a in zip(X[(i + 1):], A[i][(i + 1):]))
    print("the answer is:")
    print("\n".join("X{0} =\t{1:10.2f}".format(i + 1, x) for i, x in enumerate(X)))
    return X


def main():
    # matrix that will work for Gauss
   """" matrix = [
        [1.0, -2.0, 3.0, -4.0],
        [3.0, 3.0, -5.0, -1.0],
        [3.0, 0.0, 3.0, -10.0],
        [-2.0, 1.0, 2.0, -3.0]

    ]
    # vector
    vector = [
        2.0,
        -3.0,
        8.0,
        5.0
        ]
"""

# matrix that work for LU


matrix = [
         [5, 3, 1],
         [3, 9, 4],
         [1, 3, 5]

     ]
# vector
vector = [
        18,
        32,
        18
         ]

det = determinant(matrix)
print("the determinant is: ", det)
if det < 4:
    print("solving by Gauss:\n")
    Gauss(matrix, vector)
else:
    print("solving by LU:\n")
    L, U = lu(matrix)
    print("Matrix L:\n")
    print(L, "\n")
    print("Matrix U:\n")
    print(U)


main()
