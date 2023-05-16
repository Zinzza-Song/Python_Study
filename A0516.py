li = [list(map(int, input().split())) for _ in range(9)]


def st(a):
    for i in range(9):
        row1 = 10*[0]
        column1 = 10*[0]
        for j in range(9):
            row1[a[i][j]] = 1
            column1[a[j][i]] = 1
        if sum(row1) != 9 or sum(column1) != 9:
            return False

    for i in range(3):  #0 1 2
        for j in range(3): #0 1 2
            group1=10*[0]
            for k in range(3): #0 1 2
                for z in range(3): #0 1
                    group1[a[i*3+k][j*3+z]] = 1

            if sum(group1)!=9:
                return False
    return True


if st(li):
    print("YES")
else:
    print("NO")
