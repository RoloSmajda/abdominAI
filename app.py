import streamlit as st
from components.home import home
from components.about import about
from components.displayUI import displayUI
from components.segmentUI import segmentUI
from components.historyItem import historyItem
from datetime import datetime
from utils import *

from locales.en import en
from locales.sk import sk

def handleLocaleChange():
    if "sk" in st.session_state.selectedLocale:
        st.session_state.locales = sk
    else:
        st.session_state.locales = en


def main():
    st.set_page_config(page_title='AbdominAI', page_icon=':dna:', layout='wide')
    
    # states ---------------------------------

    if 'locales' not in st.session_state:
        st.session_state.locales = sk

    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'home'

    if 'preview_ct_path' not in st.session_state:
        st.session_state.preview_ct_path = None
    if 'preview_mask_path' not in st.session_state:
        st.session_state.preview_mask_path = None

    if 'segment_ct_path' not in st.session_state:
        st.session_state.segment_ct_path = None
    if 'segment_mask_path' not in st.session_state:
        st.session_state.segment_mask_path = None

    if 'history' not in st.session_state:  
        st.session_state.history = getHistory()

    if 'model' not in st.session_state:
        st.session_state.model = None

    if 'onlyCT' not in st.session_state:
        st.session_state.onlyCT = False


    # sidebar ---------------------------------
    with st.sidebar:
        col1, col2 = st.columns([2, 1])   
        with col1:
            home_button = st.button(st.session_state.locales["menu"]["home"], use_container_width=True)
        with col2:
            about_button = st.button(st.session_state.locales["menu"]["about"], use_container_width=True)
        displayButton = st.button(f':mag: {st.session_state.locales["menu"]["visualize"]}', use_container_width=True)
        segButton = st.button(f':gear: {st.session_state.locales["menu"]["segment"]}', use_container_width=True)

        if len(st.session_state.history) > 0:
            st.subheader(st.session_state.locales["menu"]["latest"])
            for (key, item) in enumerate(st.session_state.history):
                historyItem(key, item)

    if home_button:
        st.session_state.current_page = 'home'
    if about_button:
        st.session_state.current_page = 'about'

    if segButton:
        setSegmentPathNone()
        st.session_state.current_page = 'segmentation'
    if displayButton:
        setPreviewPathsNone()
        st.session_state.current_page = 'display'
        st.session_state.preview_id = datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
        

    #header ---------------------------------
    header = st.empty()
    if renderHeader():
        with header.container():
            col1, col2 = st.columns(2)
            with col1:
                st.title("AbdominAI", anchor=False)
                st.caption(st.session_state.locales["desc"])
            #localization ---------------------------       
            if st.session_state.current_page == 'home':
                with col2:
                    st.write('')
                    st.write('')
                    st.radio(
                        f'{st.session_state.locales["language"]}:', 
                        [f':flag-sk: {st.session_state.locales["slovak"]}', f':flag-gb: {st.session_state.locales["english"]}'], 
                        key="selectedLocale", 
                        index = 0 if st.session_state.locales['locale'] == 'sk' else 1, 
                        on_change = handleLocaleChange
                    )
    else:
        header.empty()


    # pages ---------------------------------
    if st.session_state.current_page == 'home':
        home()
    if st.session_state.current_page == 'about':
        about()
    if st.session_state.current_page == 'segmentation':
        segmentUI()
    if st.session_state.current_page == 'display':
        displayUI()

    
    


if __name__ == "__main__":
    main()