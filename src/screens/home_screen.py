import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_base_layout,style_background_home
from src.components.footer import footer_home

def home_screen():
    #st.header('Home Screen')

    header_home()
    style_background_home()
    style_base_layout()

    col1,col2 = st.columns(2,gap="large")

    with col1:
        st.header("I am Student")
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135755.png?utm_source=chatgpt.com",width=120)
        if st.button('Student Portal',type='primary',icon=':material/arrow_outward:',icon_position='right'):   
           st.session_state['login_type']='student'
           st.rerun()

    with col2:
        st.header("I am Teacher")
        st.image("https://cdn-icons-png.flaticon.com/512/1995/1995574.png?utm_source=chatgpt.com",width=120)
        if st.button('Teacher Portal',type='primary',icon=':material/arrow_outward:',icon_position='right'):
            st.session_state['login_type']='teacher'
            st.rerun()  

    footer_home()          