import cv2

# Görüntüyü yükle
image = cv2.imread('pirinc.jpg')

# Gri tonlamaya dönüştür
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Görüntüyü iyileştirme 
blur = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Eşikleme
x, thresholded = cv2.threshold(blur, 130, 255, cv2.THRESH_BINARY)

# Görüntüdeki kontürleri bul
sayi, x = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Kontür sayısını yazdır (pirinç tanelerinin sayısı)
print(f"Pirinc tanelerinin sayısı: {len(sayi)}")

# Görüntüyü ekranda göster
cv2.imshow('Pirinc Taneleri', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
