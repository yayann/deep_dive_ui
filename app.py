import streamlit as st
from PIL import Image
import requests

url = 'https://deepdive-tsahqcw5ta-ew.a.run.app/'

def get_prediction(image):
    img_bytes = image.getvalue()
    response = requests.post(url, files={"file": img_bytes})
    return response.json()

def main():
    st.title("Deep Dive: Debris Detector")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Call the API and get the prediction
        result = get_prediction(uploaded_file)

        # Check the category and display a custom message
        category = result.get("category")
        if category == "Background":
            st.write("No debris detected")
        else:
            # Use Markdown with custom styling for the category
            st.markdown(f"""
                <style>
                    .category-box {{
                        border: 1px solid #aaa;
                        border-radius: 5px;
                        padding: 5px 10px;
                        background-color: #f0f0f0;
                        display: inline-block;
                    }}
                </style>
                <div>Debris of the type <span class="category-box">{category}</span> were found in this image.</div>
                """, unsafe_allow_html=True)

        # add a spacer in between
        st.write("")
        st.write("Raw Prediction:")
        st.json(result)

if __name__ == "__main__":
    main()
