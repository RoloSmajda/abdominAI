import streamlit as st

def about():
    with st.container():
        st.write(st.session_state.locales["about"]["desc1"]) 
        st.write(st.session_state.locales["about"]["desc2"])

        col1, col2 = st.columns(2)

        with col1:
            st.subheader(f'{st.session_state.locales["about"]["organs_label"]}:', anchor=False)
            for organ in st.session_state.locales["about"]["organs"]:
                st.write(f' - {st.session_state.locales["about"]["organs"][organ]}')

        with col2:
            st.subheader("Model:", anchor=False)
            st.write(" - AbdomenAI_v1.0")
            st.caption(f'* {st.session_state.locales["about"]["segLocation"]}')

            st.metric(f'Pseudo {st.session_state.locales["dice"]}', "89,77%")
            st.metric(f'{st.session_state.locales["validation"]} {st.session_state.locales["dice"]}', "87,63%", "-2,14%", "normal")
            st.metric(f'{st.session_state.locales["test"]} {st.session_state.locales["dice"]}', "89,63%", "2%")

            st.subheader(f'{st.session_state.locales["dataset"]}:', anchor=False)
            st.write(f'- {st.session_state.locales["train"]} {st.session_state.locales["cases"]}: 300 (200 AMOS22, 50 FLARE22)')
            st.write(f' - {st.session_state.locales["test"]} {st.session_state.locales["cases"]}: 50 (AMOS22)')

        
