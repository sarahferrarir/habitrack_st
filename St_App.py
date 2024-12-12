import streamlit as st
from PIL import Image
import pickle
from PIL import Image

with open('model_new.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("🎓")
st.title("HabiTrack")

st.markdown(
    "We want to create a platform where the student will answer a quick survey about himself, telling us about how he spends his day. We will gather information about how many hours he spends studying, doing extracurricular activities, socializing, doing exercise, sleeping per day and his GPA score. Our objective is to predict a student's stress based on the info gathered about the student."
)
st.markdown("Levels of stress: 0 - Low, 1 - Moderate, 2 - High")
tab1, tab2 = st.tabs(["HabiTrack", "About us"])

with tab1:
    st.markdown("Data")
    col1, col2 = st.columns(2)
    with col1:
        Nome = st.text_input("Write your name in here:")
        Curso = st.text_input("Write your major:")
        Horas_estudo = st.number_input("How many hours do you study per day?", step=0.5)
        Horas_sono = st.number_input("What is your average sleep time?", step=0.5)
    with col2:
        Hora_extra = st.number_input("How many extracurricular activities do you do?", step=0.5)
        Hora_social = st.number_input("How many hours do you spend socializing?", step=0.5)
        Hora_physical = st.number_input("How many hours a day do you do physical activities?", step=0.5)
        gpa = st.slider("What's your GPA?", min_value=.0, max_value=4.0, step=0.01)

    X_new = [[Horas_estudo, Horas_sono, Hora_extra, Hora_social, Hora_physical, gpa]] # New data for prediction
    if st.button('Predict'):
        prediction = model.predict(X_new)

        if prediction[0] == 0:
            pred = 'Low'
        elif prediction[0] == 1:
            pred = 'Moderate'
        elif prediction[0] == 2:
            pred = 'High'

        st.title(f"Prediction student's stress: {pred}")

with tab2:
    st.markdown("Participants")
    col3, col4 =st.columns(2)
    with col3:
        st.markdown("<h2 style='text-align: center; color: white;'>Pedro </h2>",
                    unsafe_allow_html=True)

        image = Image.open('pedro.png')
        st.image(image, width=200)

        st.markdown('**Pets-**  Doggie :dog:')
        st.markdown('**Food-** Fricassê de frango')
        st.markdown('**Age-** 21 ')
        st.markdown('**Season-** Winter :snowman_without_snow:')
        st.markdown('**Movie-** Pacific Rim 🤖')
        st.markdown('**Beverage-** Root Beer 🥤')
        st.markdown('**Fruit-** Guava')
        st.link_button("Check Pedro's Linkedin",
                        "https://www.linkedin.com/in/pedrodbretasg/")
    with col4:
        st.markdown("<h2 style='text-align: center; color: white;'>Sarah </h2>",
                    unsafe_allow_html=True)

        image = Image.open('sarah.jpg')
        st.image(image, width=150)

        st.markdown('**Pets-**  Cat :cat:')
        st.markdown('**Food-** Sushi :sushi:')
        st.markdown('**Age-** 20 ')
        st.markdown('**Season-** Winter :snowman_without_snow:')
        st.markdown('**Movie-**  How to train your dragon :dragon:')
        st.markdown('**Beverage-** RedBull :coffee:')
        st.markdown('**Fruit-** Strawberry :strawberry:')
        st.link_button("Check Sarah's Linkedin",
                        "https://www.linkedin.com/in/sarahferrarir")
