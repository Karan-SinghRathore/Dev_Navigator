import streamlit as st
import pandas as pd

def profile_page():
    st.title("Profile and Progress Dashboard")

   
    st.subheader("Your Progress")
    st.progress(0.6)  
    st.write("You've completed 60% of your current roadmap!")
    
    
    st.subheader("Dashboard Metrics")

    
    st.write("## Key Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Hours", "120 hrs", "+10 hrs")
    col2.metric("Completed Modules", "24", "+2")
    col3.metric("Tasks Done", "85%", "+5%")

    
    st.write("## Detailed Progress")
    data = {
        'Module': ['Module 1', 'Module 2', 'Module 3', 'Module 4'],
        'Status': ['Completed', 'Completed', 'In Progress', 'Pending'],
        'Completion %': [100, 100, 50, 0]
    }
    progress_df = pd.DataFrame(data)
    st.table(progress_df)
    
   
    st.write("## Progress Over Time")
    trend_data = {
        'Week': ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
        'Completion %': [25, 50, 70, 85]
    }
    trend_df = pd.DataFrame(trend_data)
    st.line_chart(trend_df.set_index('Week'))