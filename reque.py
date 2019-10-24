from urllib.request import urlopen as uReq 
from bs4 import BeautifulSoup as soup
import re

def determinarFestividades(anno, pais) :
    if isinstance(anno,int) and isinstance(pais,str):
        pais = pais.lower() 
        my_url = "http://www.cuandoenelmundo.com/calendario/"+pais+"/"+str(anno)
        try:
            uClient = uReq(my_url)    
            page_html = uClient.read()
            uClient.close()

            page_soup = soup(page_html,"html.parser")
            hdays = page_soup.find('div',{'class':"hdays"})
            table = hdays.find_all('table',{'class':"hdays"})

            for element in table:  
                dia = element.find_all('td')
                dia = re.sub('<[^>]*>', '', str(dia))
                dia = dia.replace("[","")
                dia = dia.replace("]","")
                final = dia.split(',')
                i = 0
                while i < len(final):
                    print(final[i],final[i+1],final[i+2])
                    i=i+3
                    while i > len(final):
                        i = i-1
                    
        except:
            print("País o Año no disponible")
    else:
        print("Tipo de datos inválidos")



        
   


