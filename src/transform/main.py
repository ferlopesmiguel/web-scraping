import pandas as pd
import sqlite3
from datetime import datetime

pd.options.display.max_columns = None

#reading json file
df = pd.read_json('../data/data.jsonl', lines=True)

#adding new columns: source and actual date
df['source'] = 'https://lista.mercadolivre.com.br/tenis-corrida-masculino'
df['extract_date'] = datetime.now()

#replacing na and transforming in float
df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float)
df['old_price_centavos'] = df['old_price_centavos'].fillna(0).astype(float)
df['new_price_reais'] = df['new_price_reais'].fillna(0).astype(float)
df['new_price_centavos'] = df['new_price_centavos'].fillna(0).astype(float)
df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float)

#removing () from review_amount
df['reviews_amount'] = df['reviews_amount'].str.replace('[\(\)]', '', regex=True)
df['reviews_amount'] = df['reviews_amount'].fillna(0).astype(int)

#prices like float and concat int with cents
df['old_price'] = df['old_price_reais'] + df['old_price_centavos'] / 100
df['new_price'] = df['new_price_reais'] + df['new_price_centavos'] / 100

#removing columns
df.drop(columns=['old_price_reais', 'old_price_centavos', 'new_price_reais', 'new_price_centavos'], inplace=True)

#Conecting SQLite
conn = sqlite3.connect('../data/quotes.db')

#saving df
df.to_sql('quotes', conn, if_exists='replace', index=False)

conn.close()
print(df.head())