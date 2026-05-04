import streamlit as st

st.title("Diseñador de Producto")

pipeline = st.multiselect(
    "Pipeline",
    ["Auth", "RAG", "Inferencia", "Validación Humana", "Auditoría"],
    default=["Auth", "RAG", "Inferencia", "Auditoría"]
)

st.session_state["pipeline_ordered"] = pipeline

roles = st.session_state["roles"]

roles["kill_switch_owner"] = st.text_input("Kill Switch Owner")
roles["data_policy_owner"] = st.text_input("Data Policy Owner")
roles["service_owner"] = st.text_input("Service Owner")
roles["sre_owner"] = st.text_input("SRE Owner")
roles["data_steward"] = st.text_input("Data Steward")

st.session_state["roles"] = roles
