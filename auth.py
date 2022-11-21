import streamlit as st
import streamlit_authenticator as stauth
import os

ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')
USER_PASSWORD = os.environ.get('USER_PASSWORD')
SIGNATURE_KEY = os.environ.get('SIGNATURE_KEY')


def ensure_authenticated():

    usernames = {
        'usernames':
            {
                'admin': {
                    'email': 'admin@example',
                    'name': 'admin',
                    'password': ADMIN_PASSWORD
                },
                'user': {
                    'email': 'user@example.com',
                    'name': 'user',
                    'password': USER_PASSWORD
                }
            }
    }

    authenticator = stauth.Authenticate(
        usernames, 'my_app_cookie_name', SIGNATURE_KEY, 30)

    if 'authentication_status' not in st.session_state or not st.session_state['authentication_status']:
        authenticator.login('Log in', 'main')
        st.stop()
    else:
        authenticator.logout('Logout', 'sidebar')
