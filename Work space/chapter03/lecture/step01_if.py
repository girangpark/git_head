multiline='''안녕하세요. 파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀 처럼 매력적인 언어입니다.'''
cnt = 0
sents=[]
words=[]

for sent in multiline.split(sep='\n'):
    sents.append(sent)
    for word in sent.split(sep= ' '):
        words.append(word)

        print(word)
        cnt +=1
print('단어수 : ', cnt)
print(sents)
print(words)