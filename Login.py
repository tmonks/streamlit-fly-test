import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
import plotly.express as px
import yaml

# configure authenticator
with open('config.yml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

st.session_state['registering'] = st.button(
    'Click here to register', 'register')

if st.session_state['registering']:
    try:
        if authenticator.register_user('Register user', preauthorization=True):
            st.success('User registered successfully')

            # update the config file
            with open('config.yaml', 'w') as file:
                yaml.dump(config, file, default_flow_style=False)

            st.session_state['registering'] = False

    except Exception as e:
        st.error(e)

else:

    name, authentication_status, username = authenticator.login(
        'Login', 'main')

    if authentication_status:
        authenticator.logout('Logout', 'main')
        st.write(f'welcome *{name}*')

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
    elif authentication_status == False:
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username and password')
