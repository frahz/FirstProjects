matrix_a = []
matrix_b = []

size_a = input("a:")
row_a,col_a = size_a.split(" ")

for i in range(int(row_a)):
    matrix_inp = input("inside:").split(" ")
    matrix_a.append(matrix_inp)
    
size_b = input("b:")
row_b,col_b = size_b.split(" ")

if size_a == size_b:
    for i in range(int(row_b)):
        matrix_inp = input("inside:").split(" ")
        matrix_b.append(matrix_inp)

    added_matrix = []
    for i in range(int(row_a)):
        placeholder = []
        for j in range(int(col_a)):
            a_num = int(matrix_a[i][j])
            b_num = int(matrix_b[i][j])
            yopy = a_num + b_num
            placeholder.append(yopy)
        added_matrix.append(placeholder)

    for i in added_matrix:
        print (" ".join(str(x) for x in i))
else:
    print("ERROR")
