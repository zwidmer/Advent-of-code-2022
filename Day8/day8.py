import numpy as numpy

file1 = open('input8.txt', 'r')
#file1 = '30373\n25512\n65332\n33549\n35390'
Lines = file1.read().split('\n')
#Lines = file1.split('\n')

orig = numpy.array([[*line] for line in Lines])


def matr_value_comp(matrix):
    for i in numpy.arange(0, len(matrix), dtype=int):
        if i == 0 or i==len(matrix[0])-1:
            for x in numpy.arange(0, len(matrix[i]), dtype=int):
                matrix[i][x] = True
            continue
        max_in_line = -1
        last = -1
        for j in numpy.arange(0, len(matrix[i]), dtype=int):
            if (j == 0 or j==len(matrix[0])-1):
                last = int(numpy.copy(matrix[i][j]))
                max_in_line = int(numpy.copy(matrix[i][j]))
                matrix[i][j] = True
                continue
            else:
                el = int(matrix[i][j])
                if el > last and el > max_in_line:
                    last = int(numpy.copy(matrix[i][j]))
                    max_in_line = last
                    matrix[i][j] = True
                    continue
                else:
                    last = int(numpy.copy(matrix[i][j]))
                    matrix[i][j] = False
                    continue
    return matrix

def merge_lines(matrix1, matrix2):
    result = numpy.copy(matrix1)
    for x in numpy.arange(0, len(matrix2), dtype=int):
       result[x]= [a=='T' or b=='T' for a, b in zip(matrix1[x], matrix2[x])]

    return result

matrix = numpy.copy(orig)
matrixrev = numpy.copy(matrix)
matrixrev = numpy.array([list(reversed(line)) for line in matrixrev])

matrix = matr_value_comp(matrix)
matrixrev = matr_value_comp(matrixrev)

matrixrev = numpy.array([list(reversed(line)) for line in matrixrev])
print('result rev back\n', matrixrev)
print('result ori\n', matrix)
reslines = merge_lines(matrix, matrixrev)
print('merge\n', reslines)

matrixT= numpy.copy(orig).transpose()
matrixTrev = numpy.copy(matrixT)
matrixTrev = numpy.array([list(reversed(line)) for line in matrixTrev])
matrixT = matr_value_comp(matrixT)
matrixTrev = matr_value_comp(matrixTrev)
matrixTrev = numpy.array([list(reversed(line)) for line in matrixTrev])
matrixT = matrixT.transpose()
matrixTrev = matrixTrev.transpose()

rescolumns = merge_lines(matrixT, matrixTrev)


result = merge_lines(reslines, rescolumns)
print(orig)
print(result)
print(sum([list(line).count('T') for line in result]))

