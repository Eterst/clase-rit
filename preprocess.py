import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import hashlib
#Install NLTK: run: pip install --user -U nltk



archivo = open("EXTRA_23-2019,_28_NOV_17-12-2019_09_11_31.txt", encoding="utf8")
tokens = nltk.word_tokenize(archivo.read())

def borrarStopwords():
    stop_words = set(stopwords.words('spanish'))
    lemmatizer = WordNetLemmatizer()

    filtered_sentence = [w for w in tokens if not w.lower() in stop_words]

    diccionario = dict()

    for w in tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
            # Aqui se hace la lematización
            punishedW = lemmatizer.lemmatize(w)
            diccionario[hashlib.md5(punishedW.encode()).hexdigest()] = punishedW
    return filtered_sentence
#ya ni se que hace la funcion

# Ya esta borrarStopWords tambien lematiza pero :v
# deberians er funciones distintas no? :V o da igual :V 
# Di no dijo nada nada mas dijo implementar


def termSelect():
    #TODO: Opcional
    print("a")

def Tesauros():
    #TODO
    return

sin_stopwords = borrarStopwords()

print(sin_stopwords[0:20])
print("\n\n",tokens[0:20])