from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

# Extraer información de una web en este ejemplo se extrae la data de la pagina de preguntas de StackOverflow.
 
# Definimos la clase pregunta:
class pregunta(Item):
    pregunta = Field()
    id = Field()

# Definimos la araña:
class stackoverflowspider(Spider):
    name = "Mi primer Spider"
    start_urls = ["https://es.stackoverflow.com/questions"]
    def parse(self,response):
        sel = Selector (response)
        preguntas = sel.xpath('//div[@id="questions"]/div/div') # Path del tag donde se encuentran las preguntas.
        # Iteración sobre todas las preguntas.
        for i, elem in enumerate (preguntas):
            item = ItemLoader(pregunta(), elem)
            item.add_xpath('pregunta', './/h3/a/text()')# Path del tag donde se encuentra el texto de las preguntas.
            item.add_value('id',i)
            yield item.load_item()

# Una vez creado puedes ejecutarlo desde la terminal con la sentencia siguiente:
# scrapy runspider nombre_del_script.py -o nombre_del_archivo_de_datos.csv -t csv (Se guardará en la misma ruta donde
# tengamos el script de la araña).
