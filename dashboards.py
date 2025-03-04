import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Com uma visão mensal
#  faturamento por unidade...
#  tipo de produto mais vendido, contribuição por filial,
#  desempenho das formas de pagamento
#  como estão as avalições das filiais?

title = "Title um"
title

df = pd.read_csv("./assets/supermarket_sales.csv", sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df=df.sort_values("Date")

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
gender = st.sidebar.selectbox("Sexo", df["Gender"].unique())
month = st.sidebar.selectbox("Mês", df["Month"].unique())
product = st.sidebar.selectbox("Product", df["Product line"].unique())

df_filtered = df[(df["Month"] == month) & (df["Gender"] == gender) & (df["Product line"] == product)]
df_filtered

totalVendas = df_filtered["Total"].sum()
title = "totalVendas"

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(
    df_filtered,
    x="Date",
    y="Total",
    color="City",
    title="Faturamento por dia"
)
col1.plotly_chart(fig_date, use_container_width=True)

fig_prod = px.bar(
    df_filtered, 
    x="Date",
    y="Product line", 
    color="City",
    title="Faturamento por tipo de produto",
    orientation="h"
)
col2.plotly_chart(fig_prod, use_container_width=True)

city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(
    city_total, 
    x="City",
    y="Total", 
    title="Faturamento por filial",
)
col3.plotly_chart(fig_city, use_container_width=True)

fig_kind = px.pie(
    df_filtered,
    values="Total",
    names="Payment",
    title="Faturamento por tipo de pagamento"
)
col4.plotly_chart(fig_kind, use_container_width=True)

city_total = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(
    df_filtered,
    y="Rating",
    x="City",
    title="Avaliação"
)
col5.plotly_chart(fig_rating, use_container_width=True)