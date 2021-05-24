translator ={'one': 'один', 'two': 'два','three': 'три','four': 'четыре','five': 'пять',}
my_list=[]
result =[]

try:
    file_obj = open('file_4.txt','r',encoding='utf-8')
    for line in file_obj:
        splited=line.split(' - ')
        print(splited)
        if splited[0] in translator:
            word = translator.value([splited[0]])
            result.append(word +' - '+ translator.keys([splited[1]]))
    print(result)
except IOError:
    print('Произошла ошибка ввода-вывода')
file_obj.close()
try:
    file_input = open('file_2_3.txt','w')
    file_input.writelines(result)
except IOError:
    print('Произошла ошибка ввода-вывода')
file_input.close()
