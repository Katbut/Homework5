with open('created file.txt','w') as f :
    x= None
    count =1
    while x != ' ':
        x = input('Введите информацию в файл  ')
        print(x, file =f)
        count += 1