import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sqlite3

conn = sqlite3.connect("Map.db")
c = conn.cursor()

plt.figure()
img = mpimg.imread('DNDMapFinal.png')
plt.imshow(img)

roomNumber = 1
c.execute('SELECT xCoord FROM Maps WHERE roomNumber = ?', (roomNumber,))
rows = c.fetchone()
for row in rows:
    xCoord = rows

c.execute('SELECT yCoord FROM Maps WHERE roomNumber = ?', (roomNumber,))
rows = c.fetchone()
for row in rows:
    yCoord = row

plt.scatter(xCoord, yCoord, s=250, c='red', marker='o')
plt.show()

    