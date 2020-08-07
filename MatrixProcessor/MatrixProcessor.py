
def matrix_add():
    matrix_a = []
    matrix_b = []
    
    size_a = input("Enter size of first matrix:")
    row_a,col_a = size_a.split(" ")
    print("Enter first matrix:")
    for i in range(int(row_a)):
        matrix_data = input().split(" ")
        matrix_a.append(matrix_data)
    
    size_b = input("Enter size of second matrix:")
    row_b,col_b = size_b.split(" ")
    col_b *= 0 # delete later
    print("Enter second matrix:")
    if size_a == size_b:
        for i in range(int(row_b)):
            matrix_data = input().split(" ")
            matrix_b.append(matrix_data)

        output_matrix = []
        for i in range(int(row_a)):
            new_var = []
            for j in range(int(col_a)):
                a_num = int(matrix_a[i][j])
                b_num = int(matrix_b[i][j])
                sum_matrix = a_num + b_num
                new_var.append(sum_matrix)
            output_matrix.append(new_var)
        print("The result is:\n")
        for i in output_matrix:
            print (" ".join(str(x) for x in i))
    else:
        print("ERROR")

def matrix_mul_constant():
    matrix_a = []
    output_matrix = []

    size_a = input("Enter size of first matrix:")
    row_a,col_a = size_a.split(" ")
    print("Enter first matrix:")
    for i in range(int(row_a)):
        matrix_data = input().split(" ")
        matrix_a.append(matrix_data)
    
    size_b = input("Enter constant:")

    for i in range(int(row_a)):
        placeholder = []
        for j in range(int(col_a)):
            a_num = int(matrix_a[i][j])
            mul_var = a_num * int(size_b)
            placeholder.append(mul_var)
        output_matrix.append(placeholder)

    print("The result is:")
    for i in output_matrix:
        print (" ".join(str(x) for x in i))


def matrix_mul():
    print("soon TM")

while True:
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit""")

    choice = input("Your choice:")

    if choice == "1":
        matrix_add()
    elif choice == "2":
        matrix_mul_constant()
    elif choice == "3":
        matrix_mul()
    elif choice == "0":
        break
    else:
        print("Please enter valid option.")