import cv2

# Carrega a imagem em escala de cinza
image = cv2.imread("baloes-ruido.jpg", cv2.IMREAD_GRAYSCALE)

# Aplica o Filtro Laplaciano
laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Exibe a imagem resultante
cv2.imshow('Original', image)
cv2.imshow('Filtro Laplaciano', laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()

