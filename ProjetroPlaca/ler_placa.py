import cv2
import easyocr

# Caminho da imagem
imagem = "placa.jpg"

# Carregar imagem
img = cv2.imread(imagem)

# Converter para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Inicializar OCR
reader = easyocr.Reader(['pt'])

# Ler texto da imagem
resultado = reader.readtext(gray)

# Mostrar resultados
for (bbox, texto, prob) in resultado:
    print("Placa detectada:", texto)
    print("Confiança:", prob)

    # Desenhar na imagem
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple(map(int, top_left))
    bottom_right = tuple(map(int, bottom_right))

    cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
    cv2.putText(img, texto, (top_left[0], top_left[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

# Mostrar imagem
cv2.imshow("Resultado", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
