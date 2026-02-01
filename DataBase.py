from sqlalchemy import create_engine

# Sua connection string do Neon
url_banco = 'postgresql://neondb_owner:npg_ap1GTQBoSF6r@ep-curly-wildflower-ac25jj4a-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require'

engine = create_engine(url_banco)

# Enviando os dados 
try:
    df.to_sql('staging_imoveis', engine, if_exists='replace', index=False)
    print("✅ Dados brutos enviados ao Neon PostgreSQL!")
except Exception as e:
    print(f"Erro: {e}")