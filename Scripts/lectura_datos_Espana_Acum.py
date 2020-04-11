import pandas as pd 
import matplotlib.pyplot as plt

# Leemos el archivo csv que deberiamos obtener de la extracción de los casos del COVID por CCAA.
data = pd.read_csv('csv\Casos_COVID_Espana_acumulado.csv') 
# Creamos un gráfico en el que se ve la evolución de los casos totales en España desde 
# el primer caso hasta la fecha
fig, ax1=plt.subplots(figsize=(10,6))
data.plot('FECHA','CASOS')
ax1.set_xlabel("Fecha")
ax1.set_ylabel("Nº de Casos")
fig.suptitle('Casos Covid España', fontsize=15)
plt.savefig('Graficos\CasosCOVIDEspaña')
plt.show()

# Guardamos también una gráfica en la que se observa la evolución de los casos por CCAA
fig, ax2=plt.subplots(figsize=(10,6))
data_g = data.groupby('CCAA')['CASOS']
data_g.plot()
ax2.set_xlabel("Fecha")
ax2.set_ylabel("Nº de Casos")
ax2.legend(loc="best", title="CCAA", frameon=True)
fig.suptitle('Casos Covid CCAA', fontsize=15)
plt.savefig('Graficos\CasosCOVIDCCAA')
plt.show()

