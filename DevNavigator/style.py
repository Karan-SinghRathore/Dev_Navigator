import streamlit as st

def Style():
    st.markdown("""
        <style>
            /* Gradient Background with smooth subtle motion */
            body {
                font-family: 'Roboto', sans-serif;
                background: linear-gradient(135deg, #1D2B64, #F8CDDA);
                background-size: 400% 400%;
                animation: gradientBG 12s ease infinite;
                color: #EAEAEA;
                margin: 0;
                padding: 0;
                overflow-x: hidden;
            }

            /* Gradient Animation */
            @keyframes gradientBG {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            /* Sidebar Styling with hover effect */
            .sidebar .sidebar-content {
                background: rgba(44, 47, 51, 0.9);
                color: #FFFFFF;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4);
                transition: all 0.3s ease-in-out;
            }

            .sidebar .sidebar-content:hover {
                background: rgba(44, 47, 51, 1);
                box-shadow: 0 8px 15px rgba(0, 0, 0, 0.5);
            }

            /* Header Styling with Text Animation */
            h1, h2, h3 {
                font-weight: bold;
                color: #FFFFFF;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
                animation: fadeInText 2s ease-out;
            }

            /* Header text fade-in effect */
            @keyframes fadeInText {
                0% { opacity: 0; transform: translateY(30px); }
                100% { opacity: 1; transform: translateY(0); }
            }

            /* Card Hover Effects */
            .card {
                background: rgba(153, 170, 181, 0.9);
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
                margin: 10px;
                transition: all 0.4s ease-in-out;
            }

            /* Hover effect with scaling and shadow */
            .card:hover {
                background: #7289DA;
                color: #FFF;
                transform: scale(1.05) rotate(2deg);
                box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.2);
            }

            /* Button with glowing effect */
            button {
                background: linear-gradient(to right, #7289DA, #99AAB5);
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px 20px;
                font-size: 16px;
                transition: all 0.3s ease-in-out;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }

            /* Button hover effect with glow */
            button:hover {
                background: linear-gradient(to right, #4E4E50, #7289DA);
                box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
                transform: translateY(-3px);
                cursor: pointer;
                text-shadow: 0 0 10px #fff, 0 0 20px #fff;
            }

            /* Smooth Scrolling for pages */
            html {
                scroll-behavior: smooth;
            }

            /* Smooth Fade-in animation for content */
            .fade-in {
                animation: fadeIn 1.5s ease;
            }

            @keyframes fadeIn {
                0% { opacity: 0; transform: translateY(20px); }
                100% { opacity: 1; transform: translateY(0); }
            }
        </style>
    """, unsafe_allow_html=True)