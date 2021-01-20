def read_matrix(rows):
    matrix = []
    for _i in range(int(rows)):
        matrix_data = input().split(" ")
        matrix.append(matrix_data)
    return matrix


def options(func):
    # Might delete later
    if func == 1:
        print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
0. Exit""")

    elif func == 2:
        print("""1. Main Diagonal
2. Side Diagonal
3. Vertical Line
4. Horizontal Line""")

    choice = input("Your choice:")

    return choice


def print_matrix(output):
    print("The result is:\n")
    for i in output:
        print(" ".join(str(x) for x in i))


def adder():
    size_a = input("Enter size of first matrix:")
    row_a, col_a = size_a.split(" ")
    print("Enter first matrix:")
    matrix_a = read_matrix(row_a)

    size_b = input("Enter size of second matrix:")
    row_b, col_b = size_b.split(" ")
    col_b *= 0  # delete later
    print("Enter second matrix:")
    if size_a == size_b:
        matrix_b = read_matrix(row_b)

        output_matrix = []
        for i in range(int(row_a)):
            new_var = []
            for j in range(int(col_a)):
                a_num = int(matrix_a[i][j])
                b_num = int(matrix_b[i][j])
                sum_matrix = a_num + b_num
                new_var.append(sum_matrix)
            output_matrix.append(new_var)
        print_matrix(output_matrix)
    else:
        print("The operation cannot be performed.")


def mul_constant():
    size_a = input("Enter size of matrix:")
    row_a, col_a = size_a.split(" ")
    print("Enter matrix:")
    matrix_a = read_matrix(row_a)

    const = input("Enter constant:")

    output_matrix = []
    for i in range(int(row_a)):
        placeholder = []
        for j in range(int(col_a)):
            a_num = float(matrix_a[i][j])
            mul_var = a_num * float(const)
            placeholder.append(mul_var)
        output_matrix.append(placeholder)

    print_matrix(output_matrix)


def multiplier():
    size_a = input("Enter size of first matrix:")
    row_a, col_a = size_a.split(" ")
    print("Enter first matrix:")
    matrix_a = read_matrix(row_a)

    size_b = input("Enter size of second matrix:")
    row_b, col_b = size_b.split(" ")  # pylint: disable=unused-variable

    print("Enter second matrix:")
    if row_b == col_a:
        matrix_b = read_matrix(row_b)

        output_matrix = [[sum(int(a)*int(b) for a, b in zip(row_a, col_b))
                          for col_b in zip(*matrix_b)] for row_a in matrix_a]

        print_matrix(output_matrix)


def transposer():
    choice = options(2)

    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass


while True:
    choice = options(1)

    if choice == "1":
        adder()
    elif choice == "2":
        mul_constant()
    elif choice == "3":
        multiplier()
    elif choice == "4":
        transposer()
    elif choice == "0":
        break
    else:
        print("Please enter valid option.")
