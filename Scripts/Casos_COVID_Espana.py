#### Nota aclaratoria de este script ####

# El programa funciona correctamente pero ocurre algo muy extraño a lo que no le encuentro solución. Y es
# que los datos que resultan en el csv de hacer el raspado no se corresponden en absoluto a los que aparecen
# en la tabla del html de la web. Por este motivo, se ha decidido incluir el dataset de los casos acumulados
# que se puede descargar de la misma web y hacer el análisis sobre el mismo, además del archivo csv que se 
# genera ejecutando este script.

# Importamos las librerias necesarias
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Definimos la función casos_covid con la que obtendremos la tabla resumen de los casos de coronavirus por país
def casos_covid_espana():
    # Obtenemos los datos desde la url
    r = requests.get("https://covid19.isciii.es/")
    # Definimos un mensaje en caso de que no se le puedan obtener los datos
    msg = "No se pueden obtener datos"
    # Pasamos los datos a texto
    data = r.text
    # Definimos el parser
    soup = BeautifulSoup(data,'lxml')
    # Buscamos la tabla de donde extraeremos los datos
    table_body = soup.find_all('tbody')[2:][0]   

    # Definimos las condiciones que nos devolveran el mensaje de error
    if r.status_code != 200:
        return msg
    
    if not data:
        return msg
    
    if not table_body:
        return msg

    # Definimos una lista donde se almacenarán los datos
    data = []
    
    # Creamos el bucle que iterará todas las filas y las columnas (o las que queramos) de la tabla y las añadimos a la lista
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append(cols)
      
    # Definimos el DataFrame con los nombres de las columnas   
    df = pd.DataFrame(data, columns=['CCAA','Total','Ult24h','Inc.14d'])
    df.to_csv('csv\Casos_COVID_Espana.csv')    
    
    
casos_covid_espana()