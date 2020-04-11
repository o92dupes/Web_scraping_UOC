import pandas as pd 
import matplotlib.pyplot as plt

# Leemos el archivo csv que deberiamos obtener de la extracción de los casos del COVID por CCAA.
data = pd.read_csv('csv\Casos_COVID_Espana_acumulado.csv') 
# Creamos un gráfico en el que se ve la evolución de los casos totales en España desde 
# el primer caso hasta la fecha
data.plot('FECHA','CASOS')
plt.savefig('Graficos\CasosCOVIDEspaña')
plt.show()

# Guardamos también una gráfica en la que se observa la evolución de los casos por CCAA
data_g = data.groupby('CCAA')['CASOS']
data_g.plot()
plt.savefig('Graficos\CasosCOVIDCCAA')
plt.show()

