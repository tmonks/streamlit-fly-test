import streamlit as st
import auth

auth.ensure_authenticated()
st.header('Test Page')
st.markdown('This is some **amazing stuff**')
