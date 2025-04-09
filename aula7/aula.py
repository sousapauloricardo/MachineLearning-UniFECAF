# Modelo 7-gram

import numpy as np
import pandas as pd
import re
import random
from collections import defaultdict, Counter
import matplotlib.pyplot as plt

def limpar_texto(texto):
    texto = texto.lower()  # Converte tudo para minúsculas
    texto = re.sub(r'[^\w\s]', ' ', texto)  # Remove pontuações
    texto = re.sub(r'\d+', ' ', texto)      # Remove números
    texto = re.sub(r'\s+', ' ', texto)      # Substitui múltiplos espaços por um só
    return texto.strip()

class ModeloNGram:
    def __init__(self, n):
        self.n = n
        self.contagens = defaultdict(Counter)
        self.modelo = {}

    def treinar(self, palavras):
        for i in range(len(palavras) - self.n + 1):
            contexto = tuple(palavras[i:i+self.n-1])
            alvo = palavras[i+self.n-1]
            self.contagens[contexto][alvo] += 1

        for contexto, alvos in self.contagens.items():
            total = sum(alvos.values())
            self.modelo[contexto] = {
                palavra: freq / total for palavra, freq in alvos.items()
            }

    def proxima_palavra(self, contexto):
        contexto = tuple(contexto[-(self.n-1):]) if self.n > 1 else ()
        if contexto in self.modelo:
            palavras = list(self.modelo[contexto].keys())
            probs = list(self.modelo[contexto].values())
            return np.random.choice(palavras, p=probs)
        return None

    def gerar_texto(self, contexto_inicial, quantidade=15):
        if isinstance(contexto_inicial, str):
            contexto_inicial = contexto_inicial.split()
        if len(contexto_inicial) < self.n - 1:
            raise ValueError(f"Contexto inicial deve ter pelo menos {self.n - 1} palavras")
        texto = list(contexto_inicial)
        for _ in range(quantidade):
            prox = self.proxima_palavra(texto)
            if not prox:
                break
            texto.append(prox)
        return ' '.join(texto)
    
def calcular_perplexidade(modelo, texto_teste):
    tokens = limpar_texto(texto_teste).split()
    log_prob = 0
    total = 0
    for i in range(modelo.n - 1, len(tokens)):
        contexto = tuple(tokens[i - modelo.n + 1:i]) if modelo.n > 1 else ()
        alvo = tokens[i]
        prob = modelo.modelo.get(contexto, {}).get(alvo, 1e-10)
        log_prob += np.log2(prob)
        total += 1
    return 2 ** (-log_prob / total) if total > 0 else float('inf')


def mostrar_distribuicao(modelo, contexto=None):
    if modelo.n == 1:
        contexto = ()
    if contexto is None or contexto not in modelo.modelo:
        contexto = list(modelo.modelo.keys())[0]
    palavras = list(modelo.modelo[contexto].keys())
    probs = list(modelo.modelo[contexto].values())
    plt.figure(figsize=(10,5))
    plt.bar(palavras[:10], probs[:10])
    titulo = "Distribuição unigram" if modelo.n == 1 else f"Contexto: {' '.join(contexto)}"
    plt.title(titulo)
    plt.ylabel("Probabilidade")
    plt.xticks(rotation=45)
    plt.show()


def distancia_edicao(s1, s2):
    if len(s1) < len(s2):
        return distancia_edicao(s2, s1)
    if len(s2) == 0:
        return len(s1)
    anterior = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        atual = [i + 1]
        for j, c2 in enumerate(s2):
            custos = [
                anterior[j + 1] + 1,
                atual[j] + 1,
                anterior[j] + (c1 != c2)
            ]
            atual.append(min(custos))
        anterior = atual
    return anterior[-1]

# def sugerir_palavra(palavra, modelo):
#     if palavra in modelo.modelo[()]:
#         return palavra
#     candidatos = []
#     for voc in modelo.modelo[()]:
#         dist = distancia_edicao(palavra, voc)
#         if dist <= 2:
#             prob = modelo.modelo[()].get(voc, 0)
#             candidatos.append((voc, dist, prob))
#     if not candidatos:
#         return palavra
#     candidatos.sort(key=lambda x: (x[1], -x[2]))
#     return candidatos[0][0]

def sugerir_palavra(palavra, modelo_ngram, modelo_unigrama=None):
    modelo = modelo_unigrama if modelo_unigrama else modelo_ngram
    
    if () in modelo.modelo:
        if palavra in modelo.modelo[()]:
            return palavra
        
        candidatos = []
        for voc in modelo.modelo[()]:
            dist = distancia_edicao(palavra, voc)
            if dist <= 10:
                prob = modelo.modelo[()].get(voc, 0)
                candidatos.append((voc, dist, prob))
        
        if candidatos:
            candidatos.sort(key=lambda x: (x[1], -x[2]))
            return candidatos[0][0]
    
    return palavra

texto_demo = """
        A modelagem de linguagem natural é uma técnica importante no processamento de linguagem natural.
        Os modelos de linguagem podem ser usados para prever a próxima palavra em uma sequência.
        Existem diversos tipos de modelos de linguagem, incluindo modelos baseados em N-grams e modelos neurais.
        Os modelos baseados em N-grams são mais simples, mas ainda muito úteis em diversas aplicações.
"""

texto_teste = """
        Os modelos de linguagem são fundamentais para diversas aplicações.
        A modelagem estatística ajuda a entender padrões em textos.
"""



# Criação dos modelos
modelo_7gram = ModeloNGram(7)
modelo_1gram = ModeloNGram(1) 

palavras = limpar_texto(texto_demo).split()
print("Quantidade de palavras:", len(palavras))
print("Exemplo:", palavras[:51000])

modelo_7gram.treinar(palavras)
modelo_1gram.treinar(palavras)

print("Perplexidade:")
print("Unigram:", calcular_perplexidade(modelo_1gram, texto_teste))
print("Sete-gram:", calcular_perplexidade(modelo_7gram, texto_teste))




palavras_erradas = ["modelgem", "linguaem", "natual", "processment", "alongmnto"]

try:
    print("Correções sugeridas:")
    for erro in palavras_erradas:
        print(f"{erro} → {sugerir_palavra(erro, modelo_7gram, modelo_1gram)}")

except(erro):
    print(erro)

print("Textos gerados:")
print("Sete_gram:", modelo_7gram.gerar_texto(palavras[:1500], 500000))

mostrar_distribuicao(modelo_7gram)