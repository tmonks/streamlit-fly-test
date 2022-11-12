import streamlit as st
import pandas as pd
import plotly.express as px

# Import data
df = pd.read_csv('vgsales.csv')

# Group data
df_bar = df.groupby('Platform')['Global_Sales'].sum().to_frame()
df_bar.sort_values('Global_Sales', ascending=False, inplace=True)

# Streamlit content
st.title('Global Video Game Sales')
fig = px.histogram(df_bar, x=df_bar.index, y='Global_Sales')
fig.update_layout(
    xaxis_title=None,
    yaxis_title=None
)
st.plotly_chart(fig)
