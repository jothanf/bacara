from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Cambia el nombre si tu archivo es diferente
img = Image.open("Captura.JPG").convert("RGB")
arr = np.array(img)
arr = arr.reshape(-1, 3)

# Promedio de cada canal
mean_r, mean_g, mean_b = arr.mean(axis=0)
min_r, min_g, min_b = arr.min(axis=0)
max_r, max_g, max_b = arr.max(axis=0)

print(f"Promedio R: {mean_r:.1f}, G: {mean_g:.1f}, B: {mean_b:.1f}")
print(f"Mínimo   R: {min_r}, G: {min_g}, B: {min_b}")
print(f"Máximo   R: {max_r}, G: {max_g}, B: {max_b}")

# Histograma de cada canal
plt.figure(figsize=(10,4))
plt.subplot(1,3,1)
plt.hist(arr[:,0], bins=32, color='red')
plt.title('Histograma R')
plt.subplot(1,3,2)
plt.hist(arr[:,1], bins=32, color='green')
plt.title('Histograma G')
plt.subplot(1,3,3)
plt.hist(arr[:,2], bins=32, color='blue')
plt.title('Histograma B')
plt.tight_layout()
plt.show()
