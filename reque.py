from urllib.request import urlopen as uReq 
from bs4 import BeautifulSoup as soup
import re

def determinarFestividades(anno, pais) :
    my_url = "http://www.cuandoenelmundo.com/calendario/estados-unidos/2019"
    uClient = uReq(my_url)    
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html,"html.parser")
    hdays = page_soup.find('div',{'class':"hdays"})
    #table = hdays.find_all('table',{'class':"hdays"})
    
    for element in hdays:  
        dia = element.find_all('table')  #Busca los "td" que es la información necesaria
        tabl = dia[0].text.strip()
        #dia = re.sub('<[^>]*>', '', str(dia)) #Elimina toda la información innecesaria
        print(tabl)
        print(" ")

