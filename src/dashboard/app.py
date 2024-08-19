import streamlit as st
import pandas as pd
import sqlite3

#connecting db
conn = sqlite3.connect('../data/quotes.db')

#creting df
df = pd.read_sql_query("SELECT * FROM quotes", conn)

conn.close()

# Title
st.title('Pesquisa de Mercado - Tênis Esportivos no Mercado Livre')

# Better layout for columns
st.subheader('KPIs principais do sistema')
col1, col2, col3 = st.columns(3)

# KPI 1: Total items
total_itens = df.shape[0]
col1.metric(label="Número Total de Itens", value=total_itens)

# KPI 2: Unics brands
unique_brands = df['brand'].nunique()
col2.metric(label="Número de Marcas Únicas", value=unique_brands)

# KPI 3: New avg price (em reais)
average_new_price = df['new_price'].mean()
col3.metric(label="Preço Médio Novo (R$)", value=f"{average_new_price:.2f}")

# Brands with most products till 10th page
st.subheader('Marcas mais encontradas até a 10ª página')
col1, col2 = st.columns([4, 2])
top_10_pages_brands = df['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_10_pages_brands)
col2.write(top_10_pages_brands)


# Mean pirice
st.subheader('Preço médio por marca')
col1, col2 = st.columns([4, 2])
df_non_zero_prices = df[df['new_price'] > 0]
average_price_by_brand = df_non_zero_prices.groupby('brand')['new_price'].mean().sort_values(ascending=False)
col1.bar_chart(average_price_by_brand)
col2.write(average_price_by_brand)

# Brand satisfaction
st.subheader('Satisfação por marca')
col1, col2 = st.columns([4, 2])
df_non_zero_reviews = df[df['reviews_rating_number'] > 0]
satisfaction_by_brand = df_non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction_by_brand)
col2.write(satisfaction_by_brand)