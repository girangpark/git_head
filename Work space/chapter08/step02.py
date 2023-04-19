import os
print('\n현재 경로 : ', os.getcwd())

try:
    ftest1 = open('D:/pywork/Work space/chapter08/data/ftest.txt', mode = 'r')
    print(ftest1.read())

    ftest2 = open('D:/pywork/Work space/chapter08/data/ftest.txt', mode = 'w')
    ftest2.write('my first text~~~')

    ftest3 = open('D:/pywork/Work space/chapter08/data/ftest.txt', mode = 'a')
    ftest3.write('/nmy second text ~~~')

except Exception as e:
    print('Error 발생 : ', e)

finally:
    ftest1.close()
    ftest2.close()
    ftest3.close()

    
try:
    ftest = open('D:/pywork/Work space/chapter08/data/ftest.txt',mode = 'r')
    full_text = ftest.read()
    print(full_text)
    print(type(full_text))

    ftest = open('D:/pywork/Work space/chapter08/data/ftest.txt',mode= 'r')
    lines = ftest.readlines()
    print(lines)
    print(type(lines))
    print('문단수 : ', len(lines))

    docs = []
    for line in lines:
        print(line.strip())
        docs.append(line.strip())

    print(docs)

    ftest = open('D:/pywork/Work space/chapter08/data/ftest.txt', mode= 'r')
    line = ftest.readline()
    print(line)
    print(type(line))

except Exception as e:
    print('Error 발생 : ', e)

finally:
    ftest.close()