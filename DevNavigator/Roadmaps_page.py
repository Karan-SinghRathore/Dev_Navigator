import streamlit as st

def roadmaps_page():
    st.title("Hi, username 👋")
    st.subheader("Explore the Roadmaps")
    st.text_input("Search...", "")
    
    
    st.write("#### Filter by:")
    col3, col4, col5 = st.columns(3)
    with col3:
        st.button("Languages")
    with col4:
        st.button("Projects")
    with col5:
        st.button("Jobs")
    
    
    st.write("### Popular Roadmaps")
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://via.placeholder.com/200", caption="Example 1, Techstack1")
    with col2:
        st.image("https://via.placeholder.com/200", caption="Example 2, Techstack2")
    
    