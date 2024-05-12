import streamlit as st
import streamlit.components.v1 as components
import vtk
from itkwidgets import view
from ipywidgets import embed

@st.cache_resource
def render(ct_path, seg_path):
    with st.spinner(f'{st.session_state.locales["feedback"]["loading_visualization"]}...'):
        ct_scan = vtk.vtkNIFTIImageReader()
        ct_scan.SetFileName(ct_path)
        ct_scan.Update()

        if seg_path is None:
            interactive_view = view(
                image = ct_scan.GetOutput(),
                background = (255, 255, 255),
            )

        else:
            segmentation = vtk.vtkNIFTIImageReader()
            segmentation.SetFileName(seg_path)
            segmentation.Update()

            interactive_view = view(
                image = ct_scan.GetOutput(),
                label_image = segmentation.GetOutput(),
                background = (255, 255, 255),
            )

        with st.container():
            #Generate the HTML snippet for embedding
            snippet = embed.embed_snippet(
                views=interactive_view
            )
            html = embed.html_template.format(title="", snippet=snippet)

            # Display the embedded viewer in Streamlit
            components.html(html, height=800)

 