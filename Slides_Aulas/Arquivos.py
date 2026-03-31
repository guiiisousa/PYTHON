import os 

url = ["https://www.fundamentus.com.br/fii_resultado.php"]

#Inicia a URL escolhida#
def Get_fiis(url):
    os.system(f"start {url[0]}")
Get_fiis(url)
        
