import torch
from batchgenerators.utilities.file_and_folder_operations import join
from nnunetv2.inference.predict_from_raw_data import nnUNetPredictor
from nnunetv2.imageio.simpleitk_reader_writer import SimpleITKIO
import streamlit as st
import shutil



@st.cache_resource
def initializeModel():
    # instantiate the nnUNetPredictor
    predictor = nnUNetPredictor(
        tile_step_size=0.5,
        use_gaussian=True,
        use_mirroring=True,
        perform_everything_on_device=True,
        device=torch.device('cuda', 0),
        verbose=False,
        verbose_preprocessing=False,
        allow_tqdm=True
    )

    model_path = "./model/abdominAI_v1.0"

    predictor.initialize_from_trained_model_folder(
        model_path,
        use_folds=(0,),
        checkpoint_name='checkpoint_best.pth',
    )

    return predictor

def predict(predictor, predicted_mask_name):
    segment_ct_path = join(st.session_state.segment_ct_path)
    
    segment_mask_path = join(f'./data/{predicted_mask_name}')
    
    img, props = SimpleITKIO().read_images([segment_ct_path])
    predictor.predict_single_npy_array(img, props, None, segment_mask_path, False)

    #TMP just test
    # src="D:/Projects/nnUNetFrame/dataset/nnUNet_raw/Dataset250_POC/labelsTr/amos_0009.nii.gz"
    # shutil.copy(src, segment_mask_path)

    st.session_state.segment_mask_path = segment_mask_path


