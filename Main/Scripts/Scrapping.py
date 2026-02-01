import google_colab_selenium as gs
from selenium.webdriver.common.by import By
import pandas as pd
import time

 
driver = gs.Chrome()

def raspar_lopes_colab(url, cidade):
    try:
        print(f"Acessando {cidade}...")
        driver.get(url)
        time.sleep(5) 

        driver.execute_script("window.scrollTo(0, 1000);")
        time.sleep(2)

        cards = driver.find_elements(By.CSS_SELECTOR, "article, .card-listing")

        resultados = []
        for card in cards:
            try:
                # Extraindo o texto bruto
                conteudo = card.text.replace('\n', ' | ')
                if conteudo:
                    resultados.append({
                        "cidade": cidade,
                        "dados_brutos": conteudo,
                        "url_origem": url
                    })
            except:
                continue

        print(f"Sucesso: {len(resultados)} imóveis encontrados.")
        return resultados

    except Exception as e:
        print(f"Erro na extração: {e}")
        return []

url_rj = "https://www.lopes.com.br/busca/venda/br/rj/rio-de-janeiro"
dados = raspar_lopes_colab(url_rj, "Rio de Janeiro")

# Criando o DataFrame
df = pd.DataFrame(dados)
print(df.head())
