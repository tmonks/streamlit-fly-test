import streamlit as st
import streamlit_authenticator as stauth
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

try:
    if authenticator.register_user('Register user', preauthorization=True):
        st.success('User registered successfully')

        # update the config file
        with open('config.yaml', 'w') as file:
            yaml.dump(config, file, default_flow_style=False)

except Exception as e:
    st.error(e)
