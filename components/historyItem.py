import streamlit as st
from datetime import datetime
import os
from utils import getHistory

def handleLoad(ct, seg):
    st.session_state.current_page = 'display'
    st.session_state.preview_ct_path = f'./data/{ct}'
    st.session_state.preview_mask_path = f'./data/{seg}'
    st.session_state.onlyCT = False

def handleDelete(ct, seg):
    ct_path = f'./data/{ct}'
    if os.path.exists(ct_path):
        os.remove(ct_path)

    mask_path = f'./data/{seg}'
    if os.path.exists(mask_path):
        os.remove(mask_path)
    
    st.session_state.history = getHistory()


def historyItem(key, filesPair):
    ct = filesPair[0]
    seg = filesPair[1]

    datetime_string = ct.split('_')[2]
    dt = datetime.strptime(datetime_string, "%Y-%m-%d--%H-%M-%S")
    formatted_date = dt.strftime("%d %b '%y, %H:%M")


    with st.container(border=True):
        col1, col2 = st.columns([3, 2])
        with col1:
            st.subheader(ct[32:-7].replace("_0000", ""))
            st.caption(formatted_date)
        with col2:
            loadButton = st.button(st.session_state.locales["menu"]["load"], key=datetime_string, use_container_width=True, on_click=handleLoad, args=(ct, seg))
            delButton = st.button(st.session_state.locales["menu"]["delete"], key=datetime_string+"_", use_container_width=True, on_click=handleDelete, args=(ct, seg))