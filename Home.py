import streamlit as st
import pandas as pd
import plotly.express as px
import yaml
import streamlit_authenticator as stauth

with open('config.yml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

print(f'authentication_status: {st.session_state["authentication_status"]}')

if 'authentication_status' not in st.session_state or not st.session_state['authentication_status']:

    name, authentication_status, username = authenticator.login(
        'Login', 'main')
    st.stop()

authenticator.logout('Logout')

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
