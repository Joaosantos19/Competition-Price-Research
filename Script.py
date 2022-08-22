from Functions import clean_float
from Functions import clean_competition
from Functions import data_cleaning
# ---------------------- Libraries and modules -------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import pandas as pd
options = Options()
#options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#import keyboard

# ------------------------- Accessing the webpage with selenium -------------------------------
path = r"C:\Users\joaov\OneDrive\Área de Trabalho\Hashtag Cursos\Curso Python Impressionador\25. Integração Python - Automação Web (Web-Scraping com Selenium)"
Url_proj = "https://www.google.com.br/"
driver.get(Url_proj)

# ----------- Serarching the product:
table = pd.read_excel(r'Data\Tabela Geral - Reajuste.xlsx')
print(table)

for i in range(len(table)):

    try:
        # searching for the product using its EAN:
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(str(table['EAN'][i]))
        driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

        # Entering the shopping page of google:
        driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[5]/a').send_keys(Keys.ENTER)
    except:
        '''After a while google will suspect that we are a robot and will send us a "I am not a robot" thing.
        So, whenever this happens the code will close and re-open the browser and continue to run the code.
        '''
        try:
            # searching for the product using its EAN:
            driver.find_element(By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input').clear()
            driver.find_element(By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input').send_keys(str(table['EAN'][i]))
            driver.find_element(By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input').send_keys(Keys.ENTER)
        except:
            driver.close()
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            driver.get(Url_proj)

    # getting the price of the product
    try:
        table['Preco Concorrencia'][i] = clean_float(driver.find_element(By.XPATH, '//*[@id="rso"]/div/div[2]/div/div/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[2]/span/span/span[1]/span').text)
        table['Concorrencia'][i] = clean_competition(driver.find_element(By.XPATH, '//*[@id="rso"]/div/div[2]/div/div/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[3]').text)
    except:
        pass

table = data_cleaning(table)
table.to_csv('Data\Miudinho_Pesquisa.csv')
table.to_excel('Data\Miudinho Mercado.xlsx')
print('Mal feito feito')
