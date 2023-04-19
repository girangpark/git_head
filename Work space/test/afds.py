
texts_re2 = [sub("[0-9]") for text in texts]
texts_re3 = [sub('[!,.?!:;]') for text in texts_re2]
print(texts_re2)