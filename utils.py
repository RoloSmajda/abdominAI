import streamlit as st
import os

def setPreviewPathsNone():
    st.session_state.preview_ct_path = None
    st.session_state.preview_mask_path = None

def setSegmentPathNone():
    st.session_state.segment_ct_path = None
    st.session_state.segment_mask_path = None


def renderHeader():
    if st.session_state.current_page == 'home' or st.session_state.current_page == 'about':
        return True
    
    elif st.session_state.current_page == 'segmentation':
        if st.session_state.segment_ct_path is None:
            return True
        else:
            return False
        
    else: 
        if st.session_state.preview_ct_path is None or (st.session_state.preview_mask_path is None and not st.session_state.onlyCT):
            return True
        else:
            return False

def getHistory():
    ct_scans = []
    masks = []

    # get all CT and all Masks
    for filename in os.listdir('./data'):
        if 'ct' in filename:
            ct_scans.append(filename)
        if 'mask' in filename:
            masks.append(filename)

    pairs = []

    # create pairs of CT - Mask
    for ct in ct_scans:
        for mask in masks:
            if ct.split('_')[2] in mask:
                pairs.append((ct, mask, ct.split('_')[0]))
    
    # get item that dont have pair
    no_pair = ct_scans + masks
    for ct, mask, type in pairs:
        no_pair.remove(ct)
        no_pair.remove(mask)

    # remove items that dont have pairs
    for item in no_pair:
        path = f'./data/{item}'
        if os.path.exists(path):
            os.remove(path)
            

    return pairs[::-1] 
    