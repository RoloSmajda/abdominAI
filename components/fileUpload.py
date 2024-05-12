import streamlit as st
from io import BytesIO
import vtk
from itkwidgets import view
from ipywidgets import embed
import streamlit.components.v1 as components



def fileUpload(uploaded_file, fileName):
    filePath = f'./data/{fileName}.nii.gz'
    
    if uploaded_file is not None:
        # save uploaded file
        with open(filePath, "wb") as f:
            f.write(uploaded_file.getbuffer())

        return filePath
    else:
        return None
    