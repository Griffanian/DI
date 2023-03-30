input_str='without,hello,bag,world'
input_list=input_str.split(',')
input_list.sort()
out=','.join(input_list)
print(out)