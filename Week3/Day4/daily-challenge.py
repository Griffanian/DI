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

columns=''
non_alpha=0
for x in range(len(matrix[0])):
    for i,values in enumerate(list(matrix_rows)):
        if values[x].isalpha():
            columns += values[x]
            non_alpha=0
        else:
            non_alpha+=1
        if non_alpha ==2:
            columns+= ' '
    
print((columns))
        

