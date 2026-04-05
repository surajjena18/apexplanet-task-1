import pandas as pd
import streamlit as st
import plotly.express as px

# Load Excel file
df = pd.read_excel("sample_patient_data (3).xlsx")

# Title
st.title("🏥 Patient Data Dashboard")

# Show data
st.subheader("Raw Data")
st.write(df)

# -------------------------------
# 📊 1. Bar Chart (Billing Amount)
# -------------------------------
st.subheader("💰 Billing Amount per Patient")
fig1 = px.bar(df, x="Patient ID", y="Billing Amount ($)",
              color="Billing Amount ($)",
              title="Billing Distribution")
st.plotly_chart(fig1)

# -------------------------------
# 📊 2. Pie Chart (Diagnosis Status)
# -------------------------------
st.subheader("🩺 Diagnosis Status Distribution")
fig2 = px.pie(df, names="Diagnosis Status",
              title="Diagnosis Status")
st.plotly_chart(fig2)

# -------------------------------
# 📊 3. Histogram (Billing)
# -------------------------------
st.subheader("📈 Billing Amount Distribution")
fig3 = px.histogram(df, x="Billing Amount ($)",
                    nbins=10,
                    title="Billing Frequency")
st.plotly_chart(fig3)

# -------------------------------
# 📊 4. Feedback Count
# -------------------------------
st.subheader("⭐ Patient Feedback Analysis")
fig4 = px.histogram(df, x="Overall Feedback",
                    color="Overall Feedback",
                    title="Feedback Count")
st.plotly_chart(fig4)

# -------------------------------
# 📊 5. Maintenance Status
# -------------------------------
st.subheader("🔧 Maintenance Review Status")
fig5 = px.pie(df, names="Maintenance Review",
              title="Maintenance Status")
st.plotly_chart(fig5)