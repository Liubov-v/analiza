
def GaussZaidel(M, V):

    x0 = 0
    y0 = 0
    z0 = 0
    x = 0
    counter = 0     # count how many iterations
    print("X(r+1)     Y(r+1)     Z(r+1)")
    while x-x0 < 1e-5:
        x = (-M[0][1] * y0 - M[0][2] * z0 + V[0]) / M[0][0]
        y = (-M[1][0] * x - M[1][2] * z0 + V[1]) / M[1][1]
        z = (-M[2][0] * x - M[2][1] * y + V[2]) / M[2][2]
        print(x0, "  |  ", y0, "   |   ", z0)
        x0 = x
        y0 = y
        z0 = z
        counter = counter + 1
        if counter == 60:   # to make a break point
            x = 100
    return counter


def jacobi(M, V):

    x0 = 0
    y0 = 0
    z0 = 0
    x = y = z = 0
    counter = 0   # count how many iterations
    print("X(r+1)     Y(r+1)     Z(r+1)")
    while x-x0 < 1e-5:

        x = (-M[0][1]*y0-M[0][2]*z0+V[0])/M[0][0]
        y = (-M[1][0]*x0-M[1][2]*z0+V[1])/M[1][1]
        z = (-M[2][0]*x0-M[2][1]*y0+V[2])/M[2][2]
        print(x0, "  |  ", y0, "   |   ", z0)
        x0 = x
        y0 = y
        z0 = z
        counter = counter + 1
        if counter == 60:    # to make a break point
            x = 100
    return counter


def diagonal(M):
    i = 0
    m = len(M)
    k = m - 1
    x = 0
    while i < m:
        for j in range(k):
            if M[x][x] < M[j][x]:
                return False

        x = x + 1
        i = i + 1

    return True


def main():
    MyA = [[4, 2, 0],
           [2, 10, 4],
           [0, 4, 5]]

    MyX = [2, 6, 5]
    myDiagonal = diagonal(MyA)
    if not myDiagonal:
        print("The diagonal is not dominant")
    else:
        print("The diagonal is dominant")

    print("Which method would you like to choose Jacobi or Gauss Seidel")
    print("For Gauss Seidel press 1")
    print("For Jacobi press 2")
    selection = input("What do you choose")
    if selection == '1':
        a = GaussZaidel(MyA, MyX)
        print("the number of iterations is: ", a)

    if selection == '2':
        b = jacobi(MyA, MyX)
        print("the number of iterations is: ", b)


main()
