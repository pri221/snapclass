import streamlit as st

def style_background_home():

    st.markdown("""
        <style>
            .stApp{
                background: #5865F2 !important;
            }

            .stApp div[data-testid="stColumn"]{
                background-color:#E0E3FF !important;
                padding:2.5rem !important;
                border-radius:5rem !important;
            }
            
        </style>
    """, unsafe_allow_html=True)

def style_background_dashboard():

    st.markdown("""
    <style>
        .stApp{
            background: #E0E2FF !important;
        }


    </style>
    """, unsafe_allow_html=True)

def style_base_layout():

    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

        /* Hide Top Bar of streamlit */

        #MainMenu, footer, header{
            visibility: hidden;
        }
        .block-container{
            padding-top: 1.5rem !important;
        }

        h1{
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 2.0rem !important;
            line-height:1.1 !important;
            margin-bottom:0rem !important;
        }

        h2{
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 2rem !important;
            line-height:0.9 !important;
            margin-bottom:0rem !important;
            color: black !important;
        }

        h3, h4, p{
            font-family: 'outfit', sans-serif;
        }

        button{
            border-radius: 1.5rem !important;
            background: #5865F2 !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important:
            transition: transform 0.25s ease-in-out !important;
        }

        button[kind = "secondary"]{
            border-radius: 1.5rem !important;
            background: #EB459E !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important:
            transition: transform 0.25s ease-in-out !important;
        }
        
        button[kind = "tertiary"]{
            border-radius: 1.5rem !important;
            background: black !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important:
            transition: transform 0.25s ease-in-out !important;
        }

        button:hover{
            transform: scale(1.05)
        }

        /* --- INPUT FIELD STYLING ADDED HERE --- */

        /* Labels ("Enter username", "Enter password") ko Black karne ke liye */
        div[data-testid="stTextInput"] label p {
            color: black !important;
            font-weight: bold !important;
        }
        

        /* Target Streamlit text input wrapper */
        div[data-testid="stTextInput"] > div > div {
            background-color: #FFFFFF !important;
        }
        
        /* Target inner BaseWeb input elements */
        div[data-baseweb="base-input"] {
            background-color: #FFFFFF !important;
        }

        /* Target the actual input field and text color */
        div[data-testid="stTextInput"] input {
            background-color: #FFFFFF !important;
            color: #000000 !important;
        }

        /* Target placeholder text color */
        div[data-testid="stTextInput"] input::placeholder {
            color: #666666 !important;
        }

        div[data-testid="stCameraInput"] label p {
        color: #000000 !important;
        font-weight: 600;
        }


    </style>
    """, unsafe_allow_html=True)