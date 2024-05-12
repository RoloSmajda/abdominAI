import streamlit as st
import io
import sys



def home():
    with st.container():
        
        st.write('')
        st.write('')
        st.write('')
        st.write('')

        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.subheader(st.session_state.locales["features"]["platform"]["label"], anchor=False)
                st.caption(st.session_state.locales["features"]["platform"]["desc"])
            

            with st.container(border=True):
                st.subheader(st.session_state.locales["features"]["model"]["label"], anchor=False)
                st.caption(st.session_state.locales["features"]["model"]["desc"])

        with col2:
            with st.container(border=True):
                st.subheader(st.session_state.locales["features"]["tool"]["label"], anchor=False)
                st.caption(st.session_state.locales["features"]["tool"]["desc"])



            with st.container(border=True):
                st.subheader(st.session_state.locales["features"]["real-time"]["label"], anchor=False)
                st.caption(st.session_state.locales["features"]["real-time"]["desc"])
                

    
