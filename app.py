import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Page config
st.set_page_config(
    page_title="Streamlit Cloud Demo",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and introduction
st.title("🚀 Streamlit Cloud Community Demo")
st.markdown("""
This is a sample Streamlit app deployed on **Streamlit Community Cloud**.
It demonstrates various Streamlit features and best practices.
""")

# Sidebar
with st.sidebar:
    st.header("⚙️ Controls")
    
    page = st.radio(
        "Select a feature:",
        ["Home", "Data Visualization", "Interactive Form", "Data Analysis"]
    )

# Home page
if page == "Home":
    st.header("Welcome!")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Visitors", "1,234", "+12%")
    with col2:
        st.metric("Performance", "98%", "+2%")
    with col3:
        st.metric("Active Users", "567", "+23%")
    
    st.markdown("---")
    
    st.subheader("About This App")
    st.write("""
    This application showcases common Streamlit components and patterns:
    - 📊 Data visualization with charts
    - 🎛️ Interactive user inputs
    - 📈 Real-time data updates
    - 🔄 Session state management
    """)
    
    st.info("💡 Tip: Switch between different features using the sidebar menu!")

# Data Visualization page
elif page == "Data Visualization":
    st.header("📊 Data Visualization")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Line Chart")
        # Generate sample data
        dates = pd.date_range(start='2024-01-01', periods=30)
        data = pd.DataFrame({
            'Date': dates,
            'Sales': np.random.randint(100, 500, 30),
            'Revenue': np.random.randint(1000, 5000, 30)
        })
        st.line_chart(data.set_index('Date'))
    
    with col2:
        st.subheader("Bar Chart")
        categories = ['Product A', 'Product B', 'Product C', 'Product D']
        values = [120, 150, 200, 180]
        chart_data = pd.DataFrame({'Category': categories, 'Sales': values})
        st.bar_chart(chart_data.set_index('Category'))
    
    st.subheader("Data Table")
    st.dataframe(data, use_container_width=True)

# Interactive Form page
elif page == "Interactive Form":
    st.header("🎛️ Interactive Form")
    
    with st.form("user_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Email Address")
        age = st.slider("Age", 18, 100, 25)
        
        interests = st.multiselect(
            "What are your interests?",
            ["Data Science", "Web Development", "Machine Learning", "Cloud Computing"]
        )
        
        message = st.text_area("Your Message")
        
        submitted = st.form_submit_button("Submit")
    
    if submitted:
        if name and email:
            st.success("✅ Form submitted successfully!")
            st.write(f"**Name:** {name}")
            st.write(f"**Email:** {email}")
            st.write(f"**Age:** {age}")
            st.write(f"**Interests:** {', '.join(interests)}")
        else:
            st.error("❌ Please fill in all required fields")

# Data Analysis page
elif page == "Data Analysis":
    st.header("📈 Data Analysis")
    
    # Create sample dataset
    np.random.seed(42)
    dates = pd.date_range(start='2024-01-01', periods=100)
    df = pd.DataFrame({
        'Date': dates,
        'Temperature': 20 + np.random.randn(100).cumsum() * 0.5,
        'Humidity': 60 + np.random.randn(100).cumsum() * 0.3,
        'Pressure': 1013 + np.random.randn(100).cumsum() * 0.1
    })
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Avg Temperature", f"{df['Temperature'].mean():.1f}°C")
    with col2:
        st.metric("Avg Humidity", f"{df['Humidity'].mean():.0f}%")
    with col3:
        st.metric("Avg Pressure", f"{df['Pressure'].mean():.1f} hPa")
    
    st.subheader("Weather Trends")
    st.line_chart(df.set_index('Date')[['Temperature', 'Humidity']])
    
    st.subheader("Statistical Summary")
    st.dataframe(df.describe(), use_container_width=True)
    
    st.subheader("Data Export")
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download Data as CSV",
        data=csv,
        file_name="weather_data.csv",
        mime="text/csv"
    )

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>🌐 Deployed on <b>Streamlit Community Cloud</b></p>
    <p style='color: gray;'>Last updated: """ + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + """</p>
</div>
""", unsafe_allow_html=True)
