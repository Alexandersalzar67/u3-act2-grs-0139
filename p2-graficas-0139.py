
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Problema 3: Juegos
# crearemos nuestra tabla y la guardaremos con pandas

# tenemos 5 listas de juegos con 4 elementos por lista
mc  = ['Minecraft', 300, True, 2011]
gta = ['GTA V', 190, True, 2013]
tet = ['Tetris', 100, False, 1984]
wii = ['Wii Sports', 82.9, True, 2006]
pub = ['PUBG', 75, True, 2017]

# creamos una lista de listas (conformando la tabla)
lista_juegos = [mc, gta, tet, wii, pub]
print(lista_juegos)

df_juegos = pd.DataFrame(lista_juegos, columns=["Nombre", "Copias vendidas", "Es_multijugador", "Año"])
print(df_juegos)

# df_juegos.to_csv("juegos.csv", index=False)

# crear grafica de lineas
# donde x es Nombre en el eje horizontal
# donde y es Copias vendidas en el eje vertical
plt.plot(df_juegos["Nombre"], df_juegos["Copias vendidas"])
plt.title("Graficas de juegos")
plt.xlabel("Nombre de los juegos")
plt.ylabel("Copias vendidas en millones")
plt.show()

# creamos una grafica de puntos
plt.scatter(df_juegos["Nombre"], df_juegos["Copias vendidas"])
plt.show()

# graficas de barras
plt.bar(df_juegos["Nombre"], df_juegos["Copias vendidas"])
plt.title("Graficas de juegos")
plt.xlabel("Nombre de los juegos")
plt.ylabel("Copias vendidas en millones")
plt.show()

# ordenar la grafica de barras de forma descendente
# de la mas grande a la mas pequeña
df_juegos_ordenar = df_juegos.sort_values("Copias vendidas", ascending=False)
plt.bar(df_juegos_ordenar["Nombre"], df_juegos_ordenar["Copias vendidas"])
plt.show()

# coloreando la grafica
df_juegos_ordenar = df_juegos.sort_values("Copias vendidas", ascending=False)
plt.bar(df_juegos_ordenar["Nombre"], df_juegos_ordenar["Copias vendidas"],
        color=["b", "g", "c", "m", "y"])
plt.show()

# Grafica de pastel de juegos
plt.pie(df_juegos["Copias vendidas"], labels=df_juegos["Nombre"], autopct="%1.1f%%")
plt.title("Copias vendidas de videojuegos")
plt.show()
