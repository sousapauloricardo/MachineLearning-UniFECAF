# iniciar duas listas para servir de dados a serem estudados e analisados pelo algoritmo
lista1 = [1,2,3,4,5,6,7]
lista2 = [1,2,7,9,12,2,3]

# trecho para calcular as médias entre os dados de cada lista
soma1 = 0
indice = 0
for item in lista1:
    soma1 += item
    indice += 1
media1 = soma1/indice

soma2 = 0
indice = 0
for item in lista2:
    soma2 += item
    indice += 1
media2 = soma2/indice

# calculando o Beta1
somaNumerador = 0
somaDenominador = 0
for i in range(indice):
    # encontrando numerador para calculo do Beta1
    somaNumerador += (lista1[i] - media1) * (lista2[i] - media2)
    # encontrando numerador para calculo do Beta1
    somaDenominador += (lista1[i] - media1)**2
# dividindo numerador pelo denominador para descobrir o Beta1
beta1 = somaNumerador / somaDenominador

# calculando o Beta0
beta0 = media2 - (beta1 * media1)

# imprimindo os resultados encontrados
print("A média de X é: ", media1)
print("A média de Y é: ", media2)
print("O valor da reta de regressão(beta1) é: ", beta1)
print("O valor do intecepto(beta0) é: ", beta0)
