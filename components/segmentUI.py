from datetime import datetime
import streamlit as st
from components.fileUpload import fileUpload
from components.render import render
from components.predict import initializeModel, predict
import shutil


def setCtUploaded(ct_path):
    st.session_state.segment_ct_path = ct_path

def segmentUI():
    if not st.session_state.model:
        with st.spinner(f'{st.session_state.locales["feedback"]["model_init"]}...'):
            st.session_state.model = initializeModel()

    if st.session_state.segment_ct_path is None:
        col1, col2 = st.columns(2)

        if 'segment_id' not in st.session_state:
            st.session_state.segment_id = datetime.now().strftime("%Y-%m-%d--%H-%M-%S")

        with st.container():
            with col1:
                ct_file = st.file_uploader(st.session_state.locales["upload"]["ct"], type=["nii.gz"])
                if ct_file:
                    sample_name = ct_file.name.split('.')[0]
                    ct_path = fileUpload(ct_file,  f'segment_ct_{st.session_state.segment_id}_{sample_name}')
                    if ct_path is not None:
                        setCtUploaded(ct_path)

                submit = st.button(st.session_state.locales["menu"]["submit"], use_container_width=True)

                if submit and ct_file is None:
                    st.warning(st.session_state.locales["feedback"]["segment"], icon="⚠️")

    else:
        with st.spinner(f'{st.session_state.locales["feedback"]["predicting"]}...'):
            predict(st.session_state.model, f'segment_mask{st.session_state.segment_ct_path[21:]}')

        render(st.session_state.segment_ct_path, st.session_state.segment_mask_path)

    
        



