f = open('file_2.txt')
line = 0
for i in f:
    line += 1

    flag = 0
    word = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0

    print(i, len(i), 'симв.', word, 'сл.')

print(line, 'строки во всем файле')
f.close()