def pascal_ucbucagi(n):
    ucbucag = []

    for i in range(n):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = ucbucag[i - 1][j - 1] + ucbucag[i - 1][j]

        ucbucag.append(row)

    for row in ucbucag:
        print(row)

n = int(input("Pascal üçbucağındakı ədədlər sırasını daxil edin: "))
pascal_ucbucagi(n)
