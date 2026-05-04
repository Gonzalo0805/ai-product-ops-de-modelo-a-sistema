import streamlit as st

st.title("Auditoría y Reporte")

st.write("Pipeline:", st.session_state.get("pipeline_ordered"))
st.write("Roles:", st.session_state.get("roles"))
st.write("Simulación:", st.session_state.get("sim"))

st.download_button(
    "Descargar reporte",
    data=str(st.session_state),
    file_name="reporte.txt"
)
