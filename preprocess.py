import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

#Install NLTK: run: pip install --user -U nltk



archivo = open("EXTRA_23-2019,_28_NOV_17-12-2019_09_11_31.txt", encoding="utf8")
tokens = nltk.word_tokenize(archivo.read())

def borrarStopwords():
    stop_words = set(stopwords.words('spanish'))

    filtered_sentence = [w for w in tokens if not w.lower() in stop_words]
    
    filtered_sentence = []
    
    for w in tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

def lemantizarTokens():
    lemmatizer = WordNetLemmatizer()

def termSelect():
    print("a")

print(tokens[0:10])