import streamlit as st
# filename: ai_dashboard.py

import streamlit as st

# Title
st.title("AI Skills & Candidate Fit Dashboard")

# Sidebar - HR selects company requirements
st.sidebar.header("Select Company Requirements")

industry = st.sidebar.selectbox("Industry", ["Tech", "Finance", "Healthcare", "Other"])
team_size = st.sidebar.slider("Team Size", 1, 500, 10)
role_focus = st.sidebar.multiselect("Role Focus", ["Data Analysis", "Machine Learning", "Automation", "AI Research"])

st.header("Your Selected Company Requirements:")
st.write(f"Industry: {industry}")
st.write(f"Team Size: {team_size}")
st.write(f"Role Focus: {', '.join(role_focus)}")

# Skills & Experience
st.header("My Key Skills & Experience")

skills = {
    "Python": "Advanced",
    "Machine Learning": "Intermediate",
    "Data Analysis": "Advanced",
    "Workflow Automation": "Intermediate",
    "Data Visualization": "Intermediate"
}

for skill, level in skills.items():
    st.write(f"- {skill}: {level}")

# Candidate Fit Score (logic-based)
score = 50  # base
if "Machine Learning" in role_focus:
    score += 20
if "Data Analysis" in role_focus:
    score += 15
if "Automation" in role_focus:
    score += 10
if team_size < 50:
    score += 5

st.subheader("Fit Score for This Company:")
st.metric(label="Fit Score (%)", value=score)

# Projects Section
st.header("Projects Overview")
st.markdown("""
- **Customer Behavior Prediction (Confidential)**: Analyzed data, engineered features, and built predictive models to support decision-making.
- **Operational Data Analysis (Confidential)**: Developed insights from large datasets to optimize operations.
- **Mini ML Project (Public)**: [GitHub Link](https://github.com/yourusername/project)
""")

# Contact
st.header("Contact Me")
st.write("LinkedIn: [linkedin.com/in/emanmfaris](https://www.linkedin.com/in/emanmfaris)")
st.write("Email: your.email@example.com")
st.title("🎈 ENG.eman app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
