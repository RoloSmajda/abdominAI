import vtk
from itkwidgets import view
from ipywidgets import embed
import streamlit as st
import streamlit.components.v1 as components
from components.fileUpload import fileUpload
from components.render import render
from utils import getHistory

def setCtUploaded(ct_path):
    st.session_state.preview_ct_path = ct_path

def setMaskUploaded(mask_path):
    st.session_state.preview_mask_path = mask_path


def displayUI():
    if 'sample_name' not in st.session_state:
        st.session_state.sample_name = None

    if st.session_state.preview_ct_path is None or (st.session_state.preview_mask_path is None and not st.session_state.onlyCT):

        mask_file = None
            

        with st.container():
            st.toggle(st.session_state.locales["onlyCT"], key="onlyCT")
            col1, col2 = st.columns(2)

            

            with col1:
                ct_file = st.file_uploader(st.session_state.locales["upload"]["ct"], type=["nii.gz"])
                if ct_file:
                    if st.session_state.sample_name is None:
                        st.session_state.sample_name = ct_file.name.split('.')[0]
                    ct_path = fileUpload(ct_file, f'preview_ct_{st.session_state.preview_id}_{st.session_state.sample_name}')
                    if ct_path is not None:
                        setCtUploaded(ct_path)

            if not st.session_state.onlyCT:
                with col2:
                    mask_file = st.file_uploader(st.session_state.locales["upload"]["mask"], type=["nii.gz"])
                    if mask_file:
                        if st.session_state.sample_name is None:
                            st.session_state.sample_name = mask_file.name.split('.')[0]
                        mask_path = fileUpload(mask_file, f'preview_mask_{st.session_state.preview_id}_{st.session_state.sample_name}')
                        if mask_path is not None:
                            setMaskUploaded(mask_path)

                st.session_state.history = getHistory()
                
            submit = st.button(st.session_state.locales["menu"]["submit"], use_container_width=True)

            if (submit and (ct_file is None or (mask_file is None and not st.session_state.onlyCT))) or (st.session_state.onlyCT and submit and ct_file is None):
                st.warning(st.session_state.locales["feedback"]["visualize"], icon="⚠️")
                
    else:
        if not st.session_state.onlyCT:
            render(st.session_state.preview_ct_path, st.session_state.preview_mask_path)
        else:
            render(st.session_state.preview_ct_path, None)
        st.session_state.sample_name = None

    
        



