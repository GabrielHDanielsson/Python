import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

imagem = cv2.imread("carros3.jpg")

bbox, label, conf = cv.detect_common_objects(imagem)
output_image = draw_bbox(imagem, bbox, label, conf)

plt.imshow(output_image)
plt.show()

print("Numero de carros detectados: " + str(label.count('car')))

