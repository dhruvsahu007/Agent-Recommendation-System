import streamlit as st
from recommendation_engine import recommend_agents

# Streamlit App
st.title("AI Coding Agent Recommendation System")

# Task Input
task_description = st.text_area("Enter Task Description:")

if st.button("Get Recommendations"):
    if not task_description:
        st.error("Task description is required")
    else:
        recommendations = recommend_agents(task_description)
        for agent in recommendations:
            st.subheader(agent['name'])
            st.write(f"Score: {agent['score']}")
            st.write(f"Strengths: {agent['strengths']}")
