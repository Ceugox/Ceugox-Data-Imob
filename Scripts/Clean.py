import re

def limpar_dados(linha): 
    preco = re.search(r'R\$\s?([\d\.]+)', linha)
    area = re.search(r'(\d+)\s?m²', linha)

    return pd.Series({
        'preco_limpo': preco.group(1).replace('.', '') if preco else None,
        'area_limpa': area.group(1) if area else None
    })
df[['preco', 'area']] = df['dados_brutos'].apply(limpar_dados)
df['preco'] = pd.to_numeric(df['preco'])
df['area'] = pd.to_numeric(df['area'])
