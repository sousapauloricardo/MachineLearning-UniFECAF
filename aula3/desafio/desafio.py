# Importando as bibliotecas necessárias
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, roc_curve, auc
import matplotlib.pyplot as plt
import numpy as np

# Carregando o dataset Wine
wine = load_wine()
data = wine.data
target = wine.target

print ('')
print ('Data:')
print (data)
print ('')
print ('Target:')
print (target)

# Dividindo os dados em treinamento e teste
treino_teste = train_test_split(data, target,test_size=0.3, random_state=42)

# Normalizando as features


# Implementando o classificador KNN


# Calculando as métricas


# (Opcional) Plotando a Curva ROC e calculando a AUC para uma classe específica
# Para problemas multiclasse, considere a abordagem "one vs. rest".

