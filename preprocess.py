import nltk
from nltk.corpus import stopwords

#Install NLTK: run: pip install --user -U nltk

stop_words = set(stopwords.word('spanish'))

archivo = open("EXTRA_23-2019,_28_NOV_17-12-2019_09_11_31.pdf.txt")

tokens = nltk.word_tokenize(archivo.read())

filtered_sentence = [w for w in tokens if not w.lower() in stop_words]
 
filtered_sentence = []
 
for w in tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(tokens[0:10])
