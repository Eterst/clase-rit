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

# Obtenemos sinonimos con un webscrapper. No es lo mas eficiente pero nada que hacer no hay nltk español ヽ(ヅ)ノ
# Por esto mismo limitamos la cantidad de palabras que buscamos sinonimos con esta global
MAX_TESAURUS_WORDS = 5

archivo = open("EXTRA_23-2019,_28_NOV_17-12-2019_09_11_31.txt", encoding="utf8")
tokens = nltk.word_tokenize(archivo.read())

#si lematize = true va a lematizar tambien 
def borrarStopWords(lematize):
    stop_words = set(stopwords.words('spanish'))

    diccionario = dict()

    for w in tokens:
        if w not in stop_words:
            if lematize:
                lematizeWord(diccionario,w)
            else:
                filtered_sentence.append(w)
    
    filtered_sentence = list(diccionario.values())
    return filtered_sentence

# Aqui se hace la lematización
def lematizeWord(diccionario, w):
    lemmatizer = WordNetLemmatizer()
    punishedW = lemmatizer.lemmatize(w)
    diccionario[hashlib.md5(punishedW.encode()).hexdigest()] = punishedW

def selection(tokens):
    filtered_set = []
    for w in tokens:
        if w[0] == 'a' and not w[0].isnumeric() and not w[-1].isnumeric():
            filtered_set.append(w)
    return filtered_set[0:MAX_TESAURUS_WORDS]

# 🦖🦖🦖
def Tesauros(filtered_tokens):
    word_matrix = []
    for j in filtered_tokens:
        # Obtenemos sinonimos con un webscrapper. No es lo mas eficiente pero nada que hacer no hay nltk español ヽ(ヅ)ノ
        try:
            with urllib.request.urlopen('https://educalingo.com/en/dic-es/{}'.format(unidecode.unidecode(j))) as url:
                data = url.read()
                print('https://educalingo.com/en/dic-es/{}'.format(unidecode.unidecode(j)))
                final_results = re.findall('\w+', [i.text for i in soup(data, 'lxml').find_all('div', {"class":'contenido_sinonimos_antonimos0'})][0])
                word_matrix.append(final_results)
        except:
            pass

    return word_matrix

sin_stopwords = borrarStopWords(True)
filtered_set = selection(sin_stopwords)
sinonym_matrix = Tesauros(filtered_set[0:5]) #recomendado no quitar el limitante 

#print(filtered_set)
print(sinonym_matrix)
#print(sin_stopwords[0:20])
#rint("\n\n",tokens[0:20])