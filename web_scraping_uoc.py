import requests
from bs4 import BeautifulSoup
import csv

# Obtenemos codigo fuente de la web.
source = requests.get("https://experience.arcgis.com/experience/685d0ace521648f8a5beeeee1b9125cd").text
# Le decimos a Python como tiene que interpretar el código
soup = BeautifulSoup(source,'lxml')
test = soup.body.div
print(test)
# Creamos el csv donde guardaremos el data
csv_file = open('Casos_COVID.csv','w')
# Creamos el encabezado del csv
#csv_writer.writerow(['País','Número de casos confirmados'])
# Aquí irá el bucle
#for casos in soup.find_all('body'):
    #pais= soup.find('span', style = "front-size:12px")
    #print(pais)
    #casos=
    #print(casos)

    #print()

#csv.writer.writerow([pais, casos])

#csv_file.close()

