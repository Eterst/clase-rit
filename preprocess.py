from tokenize import Token
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import hashlib
import urllib
from bs4 import BeautifulSoup as soup
import re
import unidecode

# Install NLTK: run: pip install --user -U nltk
# pip install -U spacy
# python -m spacy download es_core_news_md
# pip install lxml
# pip install urllib
# pip install unidecode
# pip install bs4
# Si no funciona correr los siguientes comandos en consola de python_
#   nltk.download('wordnet')

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
        if len(w) == 7 and (w[0] == 'a' or w[0]=='d'):
            filtered_set.append(w)
    return filtered_set[0:5]

def Tesauros(filtered_tokens):
    word_matrix = []
    
    for i in filtered_tokens:
        print(i)
        with urllib.request.urlopen('https://educalingo.com/en/dic-es/{}'.format(unidecode.unidecode(i))) as url:
            data = url.read()
            print("pidio")
            final_results = re.findall('\w+', [i.text for i in soup(data, 'lxml').find_all('div', {"class":'contenido_sinonimos_antonimos0'})][0])
            word_matrix.append(final_results)

    return word_matrix

sin_stopwords = borrarStopWords(True)
filtered_set = selection(sin_stopwords)
sinonym_matrix = Tesauros(filtered_set)

#print(filtered_set)
print(sinonym_matrix)
#print(sin_stopwords[0:20])
#rint("\n\n",tokens[0:20])