import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sqlite3

class Map:

    location = 3

    def getLocation(newLocation):
        conn = sqlite3.connect("Map.db")
        c = conn.cursor()
        if(newLocation == 'NORTH'):
            c.execute('SELECT canNorth FROM Maps2 WHERE roomNumber = ?', (Map.location,))
            rows = c.fetchone()
            for row in rows:
                newRoom = row
            if( newRoom != 0):
                Map.location = newRoom
                Map.map()
            else:
                print('You ran into a wall')
        elif (newLocation == 'SOUTH'):
            c.execute('SELECT canSouth FROM Maps2 WHERE roomNumber = ?', (Map.location,))
            rows = c.fetchone()
            for row in rows:
                newRoom = row
            if(newRoom != 0):
                Map.location = newRoom
                Map.map()
            else:
                print('You ran into a wall')
        elif (newLocation == 'EAST'):
            c.execute('SELECT canEast FROM Maps2 WHERE roomNumber = ?', (Map.location,))
            rows = c.fetchone()
            for row in rows:
                newRoom = row
            if(newRoom != 0):
                Map.location = newRoom
                Map.map()
            else:
                print('You ran into a wall')
        else :
            c.execute('SELECT canWest FROM Maps2 WHERE roomNumber = ?', (Map.location,))
            rows = c.fetchone()
            for row in rows:
                newRoom = row
            if(newRoom != 0):
                Map.location = newRoom
                Map.map()
            else:
                print('You ran into a wall')
        return newRoom

    def map():

        conn = sqlite3.connect("Map.db")
        c = conn.cursor()

        plt.figure()
        img = mpimg.imread('FinalMap.jpg')
        plt.imshow(img)

        roomNumber = Map.location
        c.execute('SELECT xCoord FROM Maps2 WHERE roomNumber = ?', (roomNumber,))
        rows = c.fetchone()
        for row in rows:
            xCoord = rows

        c.execute('SELECT yCoord FROM Maps2 WHERE roomNumber = ?', (roomNumber,))
        rows = c.fetchone()
        for row in rows:
            yCoord = row
        plt.scatter(xCoord, yCoord, s=250, c='red', marker='o')
        plt.axis('off')
        plt.savefig('latestMap.png', bbox_inches='tight', pad_inches = 0)


            