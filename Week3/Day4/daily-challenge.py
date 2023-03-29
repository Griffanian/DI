matrix_str='''7i3
Tsi
h%x
i #
sM 
$a 
#t%
^r!'''
matrix_rows = matrix_str.split('\n')
matrix = [list(values) for values in list(matrix_rows)]

columns=[]
for x in range(len(matrix[0])):
    column = [values[x] for values in list(matrix_rows) if values[x].isalpha()==True]
    columns+=column
print(''.join(columns))
        

