import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TreebankWordTokenizer

# Baixar recursos necessários do NLTK
nltk.download('stopwords', download_dir='/home/codespace/nltk_data')
nltk.download('wordnet', download_dir='/home/codespace/nltk_data')
nltk.download('omw-1.4', download_dir='/home/codespace/nltk_data')  # Open Multilingual WordNet
nltk.data.path.append('/home/codespace/nltk_data')

# Baixar o recurso de stopwords
nltk.download('stopwords')

# Agora tente carregar as stopwords
from nltk.corpus import stopwords

lemmatizer = WordNetLemmatizer()
tokenizer = TreebankWordTokenizer()

palavras = ["running","better","studies","wolves","mice","children","was","ate","swimming","parties","leaves","knives","happier","studying","played","goes","driving","talked"]
palavras_lematizadas = [lemmatizer.lemmatize(token, pos='v') for token in palavras] # pos='v' declara que queremos lematizar como verbo
print('Palavras pré-definidas e lematizadas: ', palavras_lematizadas)
print('')

frases = ["The children were playing in the leaves yesterday.","She studies computer science and is taking three courses.","The wolves howled at the moon while mice scurried in the grass.","He was driving faster than the cars around him.","The chefs used sharp knives to prepare the tastiest dishes."]

stop_words = set(stopwords.words('english'))

indice = 0
for frase in frases:
    print(frase)
    print('')
    frase_tokenizada = tokenizer.tokenize(frase)
    print('Frase ',indice + 1, ' tokenizada: ', frase_tokenizada)

    print('')
    frase_stopwords = [word for word in frase_tokenizada if word in stop_words]
    print('Frase ',indice + 1, ' stopwords: ', frase_stopwords)

    print('')
    frase_sem_stopwords = [word for word in frase_tokenizada if word not in stop_words]
    print('Frase ',indice + 1, ' sem stopwords: ', frase_sem_stopwords)

    print('')
    frase_lematizada = [lemmatizer.lemmatize(token, pos='v') for token in frase_sem_stopwords]
    print('Frase ',indice + 1, ' lematizada: ', frase_lematizada)
    print('')
    indice = indice + 1





