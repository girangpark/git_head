oneLine = "this is one line string"
print(oneLine)

multiline = """this is
one line
string"""
print(multiline)

multiline2 = "this is \none line \nstring"
print(multiline2)

string = "PYTHON"
print(string[0])
print(string[5])
print(string[3])
print(string[-3])
print(string[-1])
print(string[-6])

print("python" + " " + "program")
#print("python-" + 3.7 + ".exe") 는 문자열에 실수가 더해질수 없어서 에러
print("python-" + " " + str(3.7) + ".exe")# 3.7을 문자열로 변경
print('-'*30)

print(oneLine)
print("문자열 길이 : ", len(oneLine))
print(oneLine[0:4])
print(oneLine[:4])
print(oneLine[:])
print(oneLine[::2])

print(oneLine[0:-1:2])
print(oneLine[-6:-1])
print(oneLine[-6:])

substring = oneLine[-11:]
print(substring)

print('t 글자수 : ', oneLine.count('t'))

print(oneLine.startswith('this'))
print(oneLine.startswith('that'))

print(oneLine.replace('this', 'that'))

sent = multiline.split('\n')
print('문장:', sent)

words = oneLine.split(' ')
print('단어:', words)

sent2 = ','.join(words)
print(sent2)

print('escape 문자 차단')
print('\n출력 이스케이프 문자')

print('\\n출력 이스케이프 기능 차단')
print(r'\n출력 이스케이프 기능 차단2')

print('path=', 'C:\Python\test')
print('path=', 'C:\\Python\\test')
print('path=', r'C:\Python\test')

su=5
dan=800
print('su주소 :', id(su))
print('dan 주소 :', id(dan))
print('금액=', su*dan)

x=15
if x <10 :
    print(y)
else:
    print(x)