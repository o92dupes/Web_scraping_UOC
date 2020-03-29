# Importamos las librerias necesarias
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Definimos la función casos_covid con la que obtendremos la tabla resumen de los casos de coronavirus por país
def casos_covid():
    # Obtenemos los datos desde la url
    r = requests.get("https://www.worldometers.info/coronavirus/")
    # Definimos un mensaje en caso de que no se le puedan obtener los datos
    msg = "No se pueden obtener datos"
    # Pasamos los datos a texto
    data = r.text
    # Definimos el parser
    soup = BeautifulSoup(data,'lxml')
    # Buscamos la tabla de donde extraeremos los datos
    table = soup.find("table", id = "main_table_countries_today")
   
    # Definimos las condiciones que nos devolveran el mensaje de error
    if r.status_code != 200:
        return msg
    
    if not data:
        return msg
    
    if not table:
        return msg

    # Definimos una lista donde se almacenarán los datos
    data = []
    
    # Creamos el bucle que iterará todas las filas y las columnas (o las que queramos) de la tabla y las añadimos a la lista
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append(cols)
        

 
# Definimos el DataFrame con los nombres de las columnas   
    df = pd.DataFrame(data, columns=['Pais','Casos_totales','Nuevos_casos','Muertes_totales',
    'Nuevas_muertes','Total_recuperados','Casos_activos','Casos_criticos','Casos_1M_Pop','Muertes_1M_Pop',
    'Fecha_primer_caso'])
# Convertimos El DataFrame al archivo csv deseado
    df.to_csv('Casos_COVID_mundo.csv')    
    
    
casos_covid()

