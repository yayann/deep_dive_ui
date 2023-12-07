import streamlit as st
from streamlit.components.v1 import html
from PIL import Image
import requests

url = 'https://deepdive-tsahqcw5ta-ew.a.run.app/predict'

def get_prediction(image):
    img_bytes = image.getvalue()
    response = requests.post(url, files={"file": img_bytes})
    return response.json()


def main():
    font_url = "https://fonts.googleapis.com/css2?family=Original+Surfer&display=swap"
    st.markdown(f'<link href="{font_url}" rel="stylesheet">', unsafe_allow_html=True)

    css = """
    <style>
        .mainTitle {
            font-family: 'Original Surfer', sans-serif;
            font-size: 44px;
            font-weight: bold;
        }

        .main:before {
            content: ' ';
            display: block;
            position: absolute;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            opacity: 0.6;
            background-image: url('https://i.imgur.com/GkwHy8l.jpg');
            background-repeat: no-repeat;
            background-position: 100% 50%;
            background-size: cover;
            }
    </style>
    """

    # Inject custom CSS
    st.markdown(css, unsafe_allow_html=True)

    st.markdown("<span class='mainTitle'>Deep Dive: Debris Detector</span>", unsafe_allow_html=True)

    # Sidebar
    st.sidebar.image('https://i.imgur.com/fqkbsh2.png', width=200)
    st.sidebar.markdown('<h3><a href="https://docs.google.com/presentation/d/1IhJCEaHFD1lr0hJHDOWrNU7ZuExr1K4zGb2GkyZeBXI/edit?usp=sharing">Presentation</h3>', unsafe_allow_html=True)
    st.sidebar.markdown('<h3><a href="#">Demo</h3>', unsafe_allow_html=True)
    st.sidebar.markdown('## Team Members')
    st.sidebar.markdown(""" Priyanka Gunnoo
                        <a href='https://www.linkedin.com/in/priyanka-gunnoo-2107/'><img src='https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/priyanka-gunnoo-2107/' alt='LinkedIn'></a>
                        <a href='https://github.com/piiyankag'><img src='https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=GitHub&logoColor=white&link=https://github.com/piiyankag' alt='GitHub'></a>
                        """, unsafe_allow_html=True)

    st.sidebar.markdown("""Yann Labour
                        <a href='https://www.linkedin.com/in/yannlabour//'><img src='https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/yannlabour/' alt='LinkedIn'></a>
                        <a href='https://github.com/yayann'><img src='https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=GitHub&logoColor=white&link=https://github.com/yayann' alt='GitHub'></a>
                        """, unsafe_allow_html=True)

    # Main content
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Call the API and get the prediction
        result = get_prediction(uploaded_file)

        # Check the category and display a custom message
        category = result.get("category")
        probability = result.get("probabilities")[category]

        if category == "Background":
            st.write("No debris detected")
        else:
            # Use Markdown with custom styling for the category
            st.markdown(f"""
                <style>
                    .white-bg {{ background-color: #fff; padding: 10px; border-radius: 5px; }}
                    .category-box, .proba-box  {{
                        border: 1px solid #aaa;
                        border-radius: 5px;
                        padding: 5px 10px;
                        background-color: #f0f0f0;
                        display: inline-block;
                    }}
                </style>
                <div class="white-bg">Debris of the type <span class="category-box">{category}</span> were found in this image with a probability of <span class="proba-box">{probability:.2%}.</span></div>

                """, unsafe_allow_html=True)

        # add a spacer in between
        #st.write("")
        #st.write("Raw Prediction:")
        #st.json(result)

if __name__ == "__main__":
    main()
