import streamlit as st
from ChatBot import ai_chat_page
from Profile import profile_page
from Roadmaps_page import roadmaps_page
from style import Style


Style()


st.sidebar.header("DevNavigator")
if "page" not in st.session_state:
    st.session_state["page"] = "home"

if st.sidebar.button("Home"):
    st.session_state["page"] = "home"
if st.sidebar.button("Roadmaps"):
    st.session_state["page"] = "roadmaps"
if st.sidebar.button("AI Chat"):
    st.session_state["page"] = "ai_chat"
if st.sidebar.button("Profile"):
    st.session_state["page"] = "profile"


if st.session_state["page"] == "home":
    st.title("Welcome to DevNavigator")
    
    

    
  
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("Explore Roadmaps"):
            st.session_state["page"] = "roadmaps"
            st.experimental_rerun()
    with col2:
        if st.button("Get Started"):
            st.session_state["page"] = "profile"
            st.experimental_rerun()
    with col3:
        if st.button("Jobs"):
            st.write("[Explore Jobs](https://www.indeed.com)")

elif st.session_state["page"] == "roadmaps":
    roadmaps_page()

elif st.session_state["page"] == "ai_chat":
    ai_chat_page()

elif st.session_state["page"] == "profile":
    profile_page()
