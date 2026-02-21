import streamlit as st
import joblib
import numpy as np

# Load your trained model
model = joblib.load("modelo_clasificacion_definitivo.pkl")

# --- UI ---
st.set_page_config(page_title="Text Classifier", page_icon="🤖")
st.title("🤖 Text Classifier")
st.write("Enter a text below and click **Predict** to get the model's prediction and confidence.")

text_input = st.text_area("📝 Enter your text here", height=200, placeholder="Type or paste a large text...")

if st.button("🚀 Predict", use_container_width=True):
    if not text_input.strip():
        st.warning("⚠️ Please enter some text before predicting.")
    else:
        with st.spinner("Analyzing..."):
            prediction = model.predict([text_input])[0]
            probabilities = model.predict_proba([text_input])[0]
            classes = model.classes_

        st.divider()
        st.subheader("📊 Results")

        st.markdown(f"**Prediction:** `{prediction}`")

        st.markdown("**Class Probabilities:**")
        for cls, prob in sorted(zip(classes, probabilities), key=lambda x: -x[1]):
            st.progress(float(prob), text=f"{cls}: {prob * 100:.2f}%")