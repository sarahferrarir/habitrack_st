import streamlit as st
from PIL import Image
import pickle

with open('model_new.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("HabiTrack")

st.markdown(
    "We want to create a platform where the student will answer a quick survey about himself, telling us about how he spends his day. We will gather information about how many hours he spends studying, doing extracurricular activities, socializing, doing exercise, sleeping per day and his GPA score. Our objective is to predict a student's stress based on the info gathered about the student"
)
tab1, tab2 = st.tabs(["HabiTrack", "Sobre Nós"])

with tab1:
    st.markdown("Tab1")
    col1, col2 = st.columns(2)
    with col1:
        Nome = st.text_input("Escreva aqui:")
        Curso = st.text_input("Escreva seu curso:")
        Horas_estudo = st.number_input("Quantas horas você estuda por dia?", step=0.5)
        Horas_sono = st.number_input("Média das horas de sono", step=0.5)
    with col2:
        Hora_extra = st.number_input("Quantas horas você faz de atividades extracurriculares?", step=0.5)
        Hora_social = st.number_input("Quantas horas você passa socializando?", step=0.5)
        Hora_physical = st.number_input("Quantas horas você gasta se exercitando?", step=0.5)
        gpa = st.slider("Qual seu GPA?", min_value=.0, max_value=4.0, step=0.01)

    X_new = [[Horas_estudo, Horas_sono, Hora_extra, Hora_social, Hora_physical, gpa]] # New data for prediction
    if st.button('Predict'):
        prediction = model.predict(X_new)
        st.title(f"Prediction for new student: {prediction}")


# with tab2:
#     st.markdown("Tab2")
