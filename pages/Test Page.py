import streamlit as st

if 'authentication_status' not in st.session_state or not st.session_state['authentication_status']:

    st.error('You must log in first!')
    st.markdown('Click <a href="..">here</a> to log in ')
    st.stop()

st.header('Welcome!')
