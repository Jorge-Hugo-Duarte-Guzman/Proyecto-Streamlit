import streamlit as st
import pandas as pd
ruta = 'https://github.com/Jorge-Hugo-Duarte-Guzman/practica-github/raw/refs/heads/main/BD%20Pax%20febrero%202026.csv'
df = pd.read_csv(ruta, sep=';', encoding='latin1')
st.title("Mi segunda app con Streamlit")
st.write("Este es un párrafo de prueba para la clase.")
st.dataframe(df)
st.subheader("Gráfico de pasajeros por tipo de aviación")
grafico = df.groupby('Aviacion')['Total'].sum().reset_index()
aviaciones = ['General', 'Estatal', 'Comercial Regular', 'Comercial No Regular']
grafico_filtrado = grafico[grafico['Aviacion'].isin(aviaciones)]
st.bar_chart(data=grafico_filtrado, x='Aviacion', y='Total')
print(df.columns)
