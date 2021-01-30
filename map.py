import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = np.random.randn(100, 100)

plt.figure()
img = mpimg.imread('DNDMapP.jpg')
plt.imshow(img)
#plt.annotate('25, 50', xy=(25, 50), xycoords='data',
 #            xytext=(0.5, 0.5), textcoords='figure fraction',
  #           arrowprops=dict(arrowstyle="->"))git c
plt.scatter(25, 50, s=250, c='red', marker='o')
plt.show()