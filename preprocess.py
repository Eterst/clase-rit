from tokenize import Token
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import hashlib

#Install NLTK: run: pip install --user -U nltk

archivo = open("EXTRA_23-2019,_28_NOV_17-12-2019_09_11_31.txt", encoding="utf8")
tokens = nltk.word_tokenize(archivo.read())

def borrarStopWords(lematize):
    stop_words = set(stopwords.words('spanish'))

    #filtered_sentence = [w for w in tokens if not w.lower() in stop_words]
    diccionario = dict()

    for w in tokens:
        if w not in stop_words:
            if lematize:
                lematizeWord(diccionario,w)
            else:
                filtered_sentence.append(w)
    
    filtered_sentence = list(diccionario.values())
    return filtered_sentence

def lematizeWord(diccionario, w):
    lemmatizer = WordNetLemmatizer()
    # Aqui se hace la lematización
    punishedW = lemmatizer.lemmatize(w)
    diccionario[hashlib.md5(punishedW.encode()).hexdigest()] = punishedW

def selection(tokens):
    filtered_set = []
    for w in tokens:
        if len(w) > 7:
            filtered_set.append(w)
    return filtered_set

def Tesauros():
    #TODO https://www.nltk.org/_modules/nltk/corpus/reader/lin.html
    return

sin_stopwords = borrarStopWords(True)

print(sin_stopwords[0:20])
print("\n\n",tokens[0:20])