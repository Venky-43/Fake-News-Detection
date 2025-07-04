import streamlit as st
import joblib
vectorizer = joblib.load("vectorizer.jb")
model = joblib.load("model_lr.jb")

st.title("📰 Fake News Detector")
st.write('Enter a New Article to know whether it is real or fake')

input = st.text_area("New Article:","")

if st.button("Check News"):
    if input.strip():
        tra_input = vectorizer.transform([input])
        prediction = model.predict(tra_input)

        if prediction[0]==1:
            st.success('This News is real')
        else:
            st.success('This News is Fake')
    else:
        st.warning("Please Enter some text to Analyze.")