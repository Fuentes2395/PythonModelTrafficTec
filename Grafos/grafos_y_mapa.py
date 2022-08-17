#https://networkx.org/documentation 
import networkx as nx

import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.animation as animation


salida = input("Punto de partida: ") #'1,1'
meta = input("Meta: ") #'6.3,10'

hora = input("Hora: ") 
hora = int(hora)

#https://www.youtube.com/watch?v=PouhDHfssYA 
G = nx.Graph()
if hora <= 6 or hora >= 22:
  G.add_edge("1,1", "2,7", weight=466)
  G.add_edge("2,7", "6.7,7.5", weight=347*1.5)
  G.add_edge("6.7,7.5", "6.3,10", weight=158)
  G.add_edge("6.7,7.5", "7.5,4", weight= 231.5)
  G.add_edge("7.5,4", "8,1.6", weight=231.5)
  G.add_edge("8,1.6", "9,1.8", weight=96)
  G.add_edge("8,1.6","1,1", weight=900)
  G.add_edge("9,1.8", "12,2.3", weight=202)
elif hora >= 7 or hora == 8 or hora == 10 or hora == 16 or hora == 21:
  G.add_edge("1,1", "2,7", weight=466)
  G.add_edge("2,7", "6.7,7.5", weight=347*1.5)
  G.add_edge("6.7,7.5", "6.3,10", weight=158)
  G.add_edge("6.7,7.5", "7.5,4", weight= 231.5)
  G.add_edge("7.5,4", "8,1.6", weight=231.5)
  G.add_edge("8,1.6", "9,1.8", weight=96)
  G.add_edge("8,1.6","1,1", weight=900)
  G.add_edge("9,1.8", "12,2.3", weight=202)
elif hora == 9 or hora == 11 or hora == 12 or hora == 17 or hora == 18 or hora == 19 or hora == 20:
  G.add_edge("1,1", "2,7", weight=466)
  G.add_edge("2,7", "6.7,7.5", weight=347*1.5)
  G.add_edge("6.7,7.5", "6.3,10", weight=158)
  G.add_edge("6.7,7.5", "7.5,4", weight= 231.5)
  G.add_edge("7.5,4", "8,1.6", weight=231.5)
  G.add_edge("8,1.6", "9,1.8", weight=96)
  G.add_edge("8,1.6","1,1", weight=900)
  G.add_edge("9,1.8", "12,2.3", weight=202)
elif hora == 13 or hora == 14 or hora == 15:
  G.add_edge("1,1", "2,7", weight=466)
  G.add_edge("2,7", "6.7,7.5", weight=347*1.5)
  G.add_edge("6.7,7.5", "6.3,10", weight=158)
  G.add_edge("6.7,7.5", "7.5,4", weight= 231.5)
  G.add_edge("7.5,4", "8,1.6", weight=231.5)
  G.add_edge("8,1.6", "9,1.8", weight=96)
  G.add_edge("8,1.6","1,1", weight=900)
  G.add_edge("9,1.8", "12,2.3", weight=202)


  nx.draw_networkx(G, with_labels = True)


#https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.weighted.dijkstra_path.html 
lista = nx.dijkstra_path(G, source=salida, target=meta)

lista_rutas = []

for i in range(len(lista)-1):
    if (str(lista[i]))== '1,1' and (str(lista [i+1])) == '2,7':
        lista_rutas.append(0)
    elif (str(lista[i]))== '2,7' and (str(lista [i+1])) == '6.7,7.5':
        lista_rutas.append(1)
    elif (str(lista[i]))== '6.7,7.5' and (str(lista [i+1])) == '6.3,10':
        lista_rutas.append(2)
    elif (str(lista[i]))== '6.3,10' and (str(lista [i+1])) == '7.5,4':
        lista_rutas.append(3)
    elif (str(lista[i]))== '7.5,4' and (str(lista [i+1])) == '8,1.6':
        lista_rutas.append(4)
    elif (str(lista[i]))== '8,1.6' and (str(lista [i+1])) == '9,1.8':
        lista_rutas.append(5)
    elif (str(lista[i]))== '9,1.8' and (str(lista [i+1])) == '12,2.3':
        lista_rutas.append(6)
    elif (str(lista[i]))== '12,2.3' and (str(lista [i+1])) == '1,1':
        lista_rutas.append(7)

        
    


plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()
# make data


# (1, 1) a (2, 7)
x = np.linspace(1, 2, 100)
y = 6 * x - 5

# (2, 7) a (6.7, 7.5)
x1 = np.linspace(2, 6.7, 100)
y1 = (0.5 / 4.7) * x1 + 6.79

# (6.7, 7.5) a (6.3, 10)
x2 = np.linspace(6.3, 6.7, 100)
y2 = (-6.25) * x2 + 49.375

# (6.7, 7.5) a (7.5, 4)
x3 = np.linspace(6.7, 7.5, 100)
y3 = (-4.3749) * x3 + 36.8125

# (7.5, 4) a (8, 1.6)
x4 = np.linspace(7.5, 8, 100)
y4 = (-4.8) * x4 + 40

# (8, 1.6) a (1, 1)
x5 = np.linspace(1, 8, 100)
y5 = 0.0857 * x5 + 0.9143

# (8, 1.6) a (9, 1.8)
x6 = np.linspace(8, 9, 100)
y6 = 0.2 * x6

# (9, 1.8) a (12, 2.3)
x7 = np.linspace(9, 12, 100)
y7 = 0.167 * x7 + 0.3

ax.plot(x, y, linewidth=2.0, color='black')
ax.plot(x1, y1, linewidth=2.0, color='black')
ax.plot(x2, y2, linewidth=2.0, color='black')
ax.plot(x3, y3, linewidth=2.0, color='black')
ax.plot(x4, y4, linewidth=2.0, color='black')
ax.plot(x5, y5, linewidth=2.0, color='black')
ax.plot(x6, y6, linewidth=2.0, color='black')
ax.plot(x7, y7, linewidth=2.0, color='black')

def data_gen(opciones):

    for i in opciones:
        # (1, 1) a (2, 7)
        if opciones[i]==0:
                t_max = 2.0
                dt = 0.1
                y = 0.0
                t = 1.0
                while t <= t_max:
                    y = (6 * t )-5
                    t = t + dt
                    yield t, y
        # (2, 7) a (6.7, 7.5)
        elif opciones[i]==1:
            t = 2.0
            t_max = 6.7
            dt = 0.1
            y = 0.0
            while t <= t_max:
                y = (0.5 / 4.7) * t + 6.79
                t = t + dt
                yield t, y
        # (6.7, 7.5) a (6.3, 10)
        elif opciones[i]==2:    
            t = 6.7
            t_max = 6.3
            dt = -0.1
            y = 0.0
            while t >= t_max:
                y = (-6.25) * t + 49.375
                t = t + dt
                yield t, y
        # (6.7, 7.5) a (7.5, 4)
        elif opciones[i]==3:
            t = 6.7
            t_max = 7.5
            dt = 0.1
            y = 0.0
            while t <= t_max:
                y = (-4.3749) * t + 36.8125
                t = t + dt
                yield t, y
        # (7.5, 4) a (8, 1.6)
        elif opciones[i]==4:
            t = 7.5
            t_max = 8
            dt = 0.1
            y = 0.0
            while t <= t_max:
                y = (-4.8) * t + 40
                t = t + dt
                yield t, y
        # (8, 1.6) a (1, 1)       
        elif opciones[i]==5:
            t = 8
            t_max = 1
            dt = -0.1
            y = 0.0
            while t >= t_max:
                y = 0.0857 * t + 0.9143
                t = t + dt
                yield t, y
        # (8, 1.6) a (9, 1.8)
        elif opciones[i]==6:
            t = 8
            t_max = 9
            dt = 0.1
            y = 0.0
            while t <= t_max:
                y = 0.2 * t
                t = t + dt
                yield t, y
        # (9, 1.8) a (12, 2.3)
        elif opciones[i]==7:
            t = 9
            t_max = 12
            dt = 0.1
            y = 0.0
            while t <= t_max:
                y = 0.167 * t + 0.3
                t = t + dt
                yield t, y


def init():
    ax.set_ylim(0, 15) 
    ax.set_xlim(0, 15)    
    point.set_data(0,0)
    return point,

point, = ax.plot([],[],'o',markersize=3)
ax.grid()



def run(data):
    # update the data
    t,y = data
    xdata = t
    ydata = y
    point.set_data(xdata, ydata)
    return point,





anim0 = animation.FuncAnimation(fig, run, data_gen(lista_rutas) , interval=100, init_func=init, repeat=False)
plt.show()