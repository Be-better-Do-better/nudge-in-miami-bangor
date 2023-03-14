import os
import codecs


f = codecs.open(os.path.join('..', 'Data', 'common_n_grams', 'most_common_en_words_without_shared.txt'))
t = f.read()
f.close()

s = t.split()
s1 = [w.lower() for w in s]
print(s1)
print(len(s1))

