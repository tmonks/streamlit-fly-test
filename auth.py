import streamlit as st
import streamlit_authenticator as stauth
import yaml

with open('config.yml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)


def ensure_authenticated():

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )

    if 'authentication_status' not in st.session_state or not st.session_state['authentication_status']:
        authenticator.login('Log in', 'main')
        st.stop()
    else:
        authenticator.logout('Logout', 'sidebar')
