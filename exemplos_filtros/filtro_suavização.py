import cv2
import numpy as np

valr_filtro = 3

# Carrega a imagem
#image = cv2.imread("baloes-ruido.jpg")
image = cv2.imread("baloes-pb-ruido.jpg")

# Aplica o filtro da Média
filtered_image_mean = cv2.blur(image, (valr_filtro, valr_filtro))

# Aplica o filtro da Mediana
filtered_image_median = cv2.medianBlur(image, valr_filtro)

# Aplica o filtro Gaussiano
# tamanho da matriz de suavização e 0 é o desvio padrão da distribuição gaussiana
filtered_image_gaussian = cv2.GaussianBlur(image, (valr_filtro, valr_filtro), 0)

# Exibe as imagens original e filtradas
cv2.imshow('Original', image)
cv2.imshow('Filtro da Media', filtered_image_mean)
#cv2.imshow('Filtro da Mediana', filtered_image_median)
#cv2.imshow('Filtro Gaussiano', filtered_image_gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()

